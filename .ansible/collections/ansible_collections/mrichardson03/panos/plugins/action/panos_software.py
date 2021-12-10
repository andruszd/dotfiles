# Copyright 2021 Palo Alto Networks, Inc
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import random
import time

from ansible.errors import AnsibleError
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display
from ansible_collections.mrichardson03.panos.plugins.httpapi.panos import (
    PanOSAPIError,
    TimedOutException,
)

display = Display()


class PanOSVersion(object):
    def __init__(self, version):
        try:
            (self.major, self.minor, self.patch) = version.split(".")
            self.xfr = False
        except ValueError:
            (self.major, self.minor, self.patch) = version.split(".")[0:3]
            self.xfr = True

        self.major = int(self.major)
        self.minor = int(self.minor)

    def __eq__(self, other):
        if (
            self.major == other.major
            and self.minor == other.minor
            and self.patch == other.patch
        ):
            return True
        else:
            return False

    def __str__(self):
        s = f"{self.major}.{self.minor}.{self.patch}"

        if self.xfr:
            s += ".xfr"

        return s


def is_valid_upgrade(current, target):
    # Patch version upgrade (major and minor versions match)
    if (current.major == target.major) and (current.minor == target.minor):
        return True

    # Upgrade minor version (9.0.0 -> 9.1.0)
    elif (current.major == target.major) and (current.minor + 1 == target.minor):
        return True

    # Upgrade major version (9.1.0 -> 10.0.0)
    elif (current.major + 1 == target.major) and (target.minor == 0):
        return True

    else:
        return False


class ActionModule(ActionBase):
    TRANSFERS_FILES = False
    _VALID_ARGS = frozenset(
        ["version", "sync_to_peer", "download", "install", "restart", "timeout"]
    )

    def _do_download(self, cmd, timeout):
        try:
            self._connection.op(cmd, poll=True, poll_interval=10, poll_timeout=timeout)

        except PanOSAPIError as exc:
            if "try again later" in exc.message:
                display.debug(
                    "panos_software: Got try again message, trying random wait"
                )

                # Randomly wait between one and five minutes.
                time.sleep(random.randint(1, 5) * 60)

                self._connection.op(
                    cmd, poll=True, poll_interval=10, poll_timeout=timeout
                )
            else:
                raise AnsibleError(exc.message)

    def _do_upgrade(
        self,
        current,
        target,
        sync_to_peer=True,
        download=True,
        install=True,
        timeout=600,
    ):
        display.debug(f"panos_software: performing upgrade ({current} -> {target})")

        random.seed()

        cmd = "<request><system><software><check></check></software></system></request>"
        self._connection.op(cmd)

        if download and (
            (current.major != target.major) or (current.minor != target.minor)
        ):
            base = PanOSVersion(f"{target.major}.{target.minor}.0")
            display.debug(f"panos_software: download new base version: {base}")

            cmd = (
                f"<request><system><software><download>"
                f"<version>{base}</version>"
                f"<sync-to-peer>{'yes' if sync_to_peer else 'no'}</sync-to-peer>"
                f"</download></software></system></request>"
            )

            try:
                self._do_download(cmd, timeout)
            except TimedOutException:
                raise AnsibleError("Timeout while downloading new base version.")

        if download:
            display.debug(f"panos_software: download target version: {target}")

            cmd = (
                f"<request><system><software><download>"
                f"<version>{target}</version>"
                f"<sync-to-peer>{'yes' if sync_to_peer else 'no'}</sync-to-peer>"
                f"</download></software></system></request>"
            )

            try:
                self._do_download(cmd, timeout)
            except TimedOutException:
                raise AnsibleError("Timeout while downloading new target version.")

        if install:
            display.debug(f"panos_software: install target version: {target}")
            cmd = (
                f"<request><system><software><install>"
                f"<version>{target}</version>"
                f"</install></software></system></request>"
            )

            try:
                self._connection.op(
                    cmd, poll=True, poll_interval=10, poll_timeout=timeout
                )
            except TimedOutException:
                raise AnsibleError("Timeout while installing new target version.")

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp

        if "version" not in self._task.args:
            raise AnsibleError("'version' is required")

        target = PanOSVersion(self._task.args.get("version"))
        sync_to_peer = bool(self._task.args.get("sync_to_peer", True))
        download = bool(self._task.args.get("download", True))
        install = bool(self._task.args.get("install", True))
        restart = bool(self._task.args.get("restart", False))
        timeout = int(self._task.args.get("timeout", 600))

        current = PanOSVersion(self._connection.version()["sw-version"])

        if target != current:
            result["changed"] = True
            verb = "Installed" if install else "Downloaded"
            result["msg"] = f"{verb} PAN-OS version {target}."

            if not is_valid_upgrade(current, target):
                raise AnsibleError("upgrade is invalid: ({current} -> {target})")

            if not self._play_context.check_mode:
                self._do_upgrade(
                    current,
                    target,
                    sync_to_peer=sync_to_peer,
                    download=download,
                    install=install,
                    timeout=timeout,
                )

            if restart:
                display.debug("panos_software: restarting device")

                if not self._play_context.check_mode:
                    self._connection.op("request restart system", is_xml=False)

        return result
