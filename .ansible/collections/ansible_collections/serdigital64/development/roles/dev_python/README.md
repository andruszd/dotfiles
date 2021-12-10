---
title: "Ansible Role: serdigital64.development.dev_python"
description: "Manage provision of Python"
authors:
  - SerDigital64
tags:
  - ansible
  - devops
  - linux
  - automation
---

# Ansible Role: serdigital64.development.dev_python

## Purpose

Manage provision of Python

Supported features in the current version:

- Deploy language. Packages are defined in the variable `dev_python_profiles`.

The **dev_python** Ansible-Role is part of the [A:Platform64](https://aplatform64.readthedocs.io) project and is available in the [development](../collections/development.md) Ansible-Collection.

## Use Cases

### Install application Python

```yaml
- name: "Example: Install Python"
  vars:
    dev_python:
      resolve_prereq: true
      deploy: true
  ansible.builtin.include_role:
    name: "serdigital64.development.dev_python"
```

## Role Parameters

### Actions

- Use **action-parameters** to control what tasks are enabled for the role to execute.
- Parameters should be declared as task level vars as they are intented to be dynamic.

```yaml
dev_python:
  resolve_prereq:
  deploy:
```

| Parameter                 | Required? | Type    | Default | Purpose / Value                             |
| ------------------------- | --------- | ------- | ------- | ------------------------------------------- |
| dev_python.resolve_prereq | no        | boolean | `false` | Enable automatic resolution of prequisites  |
| dev_python.deploy         | no        | boolean | `false` | Enable installation of application packages |

### End State

- Use **end-state** parameters to define the target state after role execution.
- Parameters should be declared in **host_vars** or **group_vars** as they are intended to be permanent.

```yaml
dev_python_application:
  name:
  type:
  version:
  installed:
```

| Parameter                        | Required? | Type       | Default    | Purpose / Value                    |
| -------------------------------- | --------- | ---------- | ---------- | ---------------------------------- |
| dev_python_application           | no        | dictionary |            | Set application package end state  |
| dev_python_application.name      | no        | string     | `"python"` | Select application package name    |
| dev_python_application.type      | no        | string     | `"distro"` | Select application package type    |
| dev_python_application.version   | no        | string     | `"latest"` | Select application package version |
| dev_python_application.installed | no        | boolean    | `true`     | Set application package end state  |

## Deployment

### OS Compatibility

- CentOS8
- OracleLinux8
- Ubuntu20
- Ubuntu21
- Fedora33
- Debian10
- Debian11

### Dependencies

- Ansible Collections:
  - serdigital64.core

### Prerequisites

All the prerequisites listed in this section can be automatically resolved by enabling the role action `resolve_prereq: true`

- Package managers for the target application are installed and enabled.
- **A:Platform64** package installer (core_package) runtime environment is ready.

### Installation Procedure

The role can be deployed by installing the Ansible-Collection from the Ansible Galaxy repository: [https://galaxy.ansible.com/serdigital64/development](https://galaxy.ansible.com/serdigital64/development)

```shell
# Install Ansible dependencies
ansible-galaxy collection install serdigital64.core
# Install the collection
ansible-galaxy collection install serdigital64.development
```

## Contributing

Help on implementing new features and maintaining the code base is welcomed.

Please see the [guidelines](../contributing/guidelines.md) for further details.

## Author

- [SerDigital64](https://github.com/serdigital64)

## License

[GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0.txt)
