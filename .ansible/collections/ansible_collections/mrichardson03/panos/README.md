# PAN-OS Ansible Collection - mrichardson03.panos

![GitHub Actions](https://github.com/mrichardson03/mrichardson03.panos/workflows/CI/badge.svg)
![Version on Galaxy](https://img.shields.io/badge/dynamic/json?style=flat&label=Ansible+Galaxy&prefix=v&url=https://galaxy.ansible.com/api/v2/collections/mrichardson03/panos/&query=latest_version.version)

Ansible collection for automating configuration and maintenance tasks on Palo Alto Networks Next Generation Firewalls.

Documentation: https://mrichardson03.github.io/mrichardson03.panos/

## How is this different than paloaltonetworks.panos?

This collection is different than the official Palo Alto Networks collection in a number of key ways:

- **Direct XML API support.** All aspects of PAN-OS can be configured using the standard Ansible Jinja2 templating
  language.
- **Uses standard Ansible connection methods.** This collection is written using as an Ansible httpapi plugin. This
  allows for a number of enhancements, most notably persistent connections to the device.
- **Minimal dependencies.** Only uses `requests` and `xmltodict`.

This collection is **not backwards compatible** with `paloaltonetworks.panos`.

## Python Compatability

This collection is written for Python 3.8, which is the version used in the
default Ansible AWX virtual environment. Newer versions of Python will likely
work, but are not tested.
