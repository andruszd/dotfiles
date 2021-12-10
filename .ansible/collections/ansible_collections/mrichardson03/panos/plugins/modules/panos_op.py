#!/usr/bin/python

# Copyright 2020 Palo Alto Networks, Inc
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

DOCUMENTATION = """
---
module: panos_op
short_description: Execute an operational command on PAN-OS devices.
description:
    - Allows a user to execute an operational command on a PAN-OS device.
author:
    - 'Michael Richardson (@mrichardson03)'
version_added: '1.0.0'
requirements:
    - xmltodict
notes:
    - Check mode is NOT supported.
options:
    cmd:
        description:
            - Operational command to run.
        type: str
        required: true
    cmd_is_xml:
        description:
            - If C(true), treat the cmd option as a string already in XML format. If C(false), attempt to convert it to
              XML before execution.
        type: bool
        default: false
"""

EXAMPLES = """
- name: show system info
  panos_op:
    cmd: 'show system info'

- name: show system info (as XML)
  panos_op:
    cmd: '<show><system><info/></system></show>'
    cmd_is_xml: true
"""

RETURN = """
changed:
    description:
        - A boolean value indicating if the task had to make changes. Commands starting with C(diff) and C(show) are
          deemed to be safe, and will return C(false).  All others will return C(true).
    returned: always
    type: bool

stdout:
    description: Output of the command in native XML format.
    returned: always
    type: str
    sample: "<response status=success><result><system><hostname>fw2</hostname>"

stdout_dict:
    description: Output of 'cmd', converted into a dictionary format.
    returned: always
    type: dict
    sample: >
        {
            'response': {
                '@status': 'success',
                'result': {
                    'system': {
                        'hostname': 'fw2',
                        ...
                    }
                }
            }
        }
"""

try:
    import xmltodict

    HAS_LIB = True
except ImportError:  # pragma: no cover
    HAS_LIB = False

from ansible.module_utils.connection import ConnectionError
from ansible_collections.mrichardson03.panos.plugins.module_utils.panos import (
    PanOSAnsibleModule,
)


def main():
    module = PanOSAnsibleModule(
        argument_spec=dict(
            cmd=dict(type="str", required=True),
            cmd_is_xml=dict(default=False, type="bool"),
        ),
        supports_check_mode=False,
    )

    if not HAS_LIB:  # pragma: no cover
        module.fail_json(msg="Missing required libraries.")

    cmd = module.params["cmd"]
    cmd_is_xml = module.params["cmd_is_xml"]

    results = None

    try:
        changed = True

        safe_cmds = ["diff", "show"]
        safe_xml_cmds = ["<diff>", "<show>"]

        if cmd_is_xml:
            for safe_xml_cmd in safe_xml_cmds:
                if cmd.find(safe_xml_cmd) == 0:
                    changed = False

        else:
            for safe_cmd in safe_cmds:
                if cmd.find(safe_cmd) == 0:
                    changed = False

        xml_output = module.connection.op(cmd, is_xml=cmd_is_xml)
        obj_dict = xmltodict.parse(xml_output)

        results = {"changed": changed, "stdout": xml_output, "stdout_dict": obj_dict}
        module.exit_json(**results)

    except ConnectionError as e:  # pragma: no cover
        module.fail_json(msg=f"{e}")


if __name__ == "__main__":  # pragma: no cover
    main()
