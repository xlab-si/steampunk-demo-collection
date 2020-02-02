#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2020, XLAB Steampunk <steampunk@xlab.si>
#
# Apache License v2.0 (see https://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["stableinterface"],
    "supported_by": "community",
}

DOCUMENTATION = """
module: marker
author:
  - Tadej Borovsak (@tadeboro)
short_description: Manage marker files
description:
  - Manage marker files with user-defined content.
version_added: "1.0"
options:
  path:
    description:
      - Location of the marker file.
    type: str
    required: true
  state:
    description:
      - Target state of the marker file.
    type: str
    choices: [ present, absent ]
    default: present
  content:
    description:
      - The marker file content.
    type: str
    default: MARKER
"""

EXAMPLES = """
- name: Make sure marker file with default content is present
  steampunk.demo.marker:
    path: /tmp/marker

- name: Make sure marker file with custom content is present
  steampunk.demo.marker:
    path: /tmp/marker
    content: >
      A long marker line that is split here because we can do that in YAML
      documtnts, so we did it.

- name: Delete marker file if it is present on the system
  steampunk.demo.marker:
    path: /tmp/marker
    state: absent
"""

RETURN = """ # """

import os

from ansible.module_utils.basic import AnsibleModule


try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError  # Python2 compatibility


def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            path=dict(
                required=True,
            ),
            state=dict(
                choices=["present", "absent"],
                default="present",
            ),
            content=dict(
                default="MARKER",
            ),
        ),
    )

    if module.params["state"] == "present":
        try:
            with open(module.params["path"]) as fd:
                existing_content = fd.read()
        except FileNotFoundError:
            existing_content = ""

        changed = existing_content != module.params["content"]
        if changed and not module.check_mode:
            with open(module.params["path"], "w") as fd:
                fd.write(module.params["content"])
    else:
        changed = os.path.isfile(module.params["path"])
        if changed and not module.check_mode:
            os.remove(module.params["path"])

    module.exit_json(changed=changed)


if __name__ == "__main__":
    main()
