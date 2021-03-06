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

import re
from functools import reduce

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection


class PanOSAnsibleModule(AnsibleModule):
    def __init__(
        self,
        argument_spec,
        api_endpoint=None,
        with_state=False,
        with_enabled_state=False,
        *args,
        **kwargs,
    ):
        spec = {}

        self.api_endpoint = api_endpoint

        if with_state:
            spec["state"] = {"default": "present", "choices": ["present", "absent"]}

        if with_enabled_state:
            spec["state"] = {
                "default": "present",
                "choices": ["present", "absent", "enabled", "disabled"],
            }

        argument_spec.update(spec)

        super().__init__(argument_spec, *args, **kwargs)

        self.connection = Connection(self._socket_path)


def cmd_xml(cmd):
    def _cmd_xml(args, obj):
        if not args:
            return
        arg = args.pop(0)
        if args:
            result = re.search(r'^"(.*)"$', args[0])
            if result:
                obj.append(f"<{arg}>")
                obj.append(result.group(1))
                obj.append(f"</{arg}>")
                args.pop(0)
                _cmd_xml(args, obj)
            else:
                obj.append(f"<{arg}>")
                _cmd_xml(args, obj)
                obj.append(f"</{arg}>")
        else:
            obj.append(f"<{arg}>")
            _cmd_xml(args, obj)
            obj.append(f"</{arg}>")

    args = cmd.split()
    obj = []
    _cmd_xml(args, obj)
    xml = "".join(obj)

    return xml


def get_nested_key(d, key_list):
    """
    Access a nested key within a dictionary safely.

    Example:

    For the dictionary d = {'one': {'two': {'three': 'four'}}},
    get_nested_key(d, ['one', 'two', 'three']) will return 'four'.

    :param d: Dictionary
    :param key_list: List of keys, in decending order.
    """

    return reduce(lambda val, key: val.get(key) if val else None, key_list, d)
