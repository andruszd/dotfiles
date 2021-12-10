.. _onboard_role:

onboard
=======

Performs initial PAN-OS configuration steps. Useful for when bootstrapping can't be used.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with any default values (see ``defaults/main.yml``). If no values are
listed, the variable is not defined by default and will not be configured.

.. code-block:: yaml+jinja

    ready_timeout: 600

Maximum amount of time (in seconds) to poll the device to see if it is ready for configuration.

.. code-block:: yaml+jinja

    dns_primary: 8.8.8.8
    dns_secondary: 8.8.4.4

Configures DNS for the device to these values.

.. code-block:: yaml+jinja

    authcode:

When set, the device will be licensed.

.. code-block:: yaml+jinja

    install_content: True

Upgrades content to the latest available version.

.. code-block:: yaml+jinja

    licensing_api_key:

When set, set the Licensing API key associated with your support account on the device. This is useful for deactivating
VM-Series firewalls later.

.. code-block:: yaml+jinja

    version:

When set, upgrade PAN-OS on the device to this version. This upgrade should only be one PAN-OS version different from
the one currently running (example: 9.1.3 -> 10.0.2).

.. code-block:: yaml+jinja

    software_timeout: 600

Maximum amount of time (in seconds) each software download or installation job performed by this module is allowed to
run before error.  A single call to ``panos_software`` can potentially trigger two download jobs and a single install
job in the case of a full upgrade, so this step can potentially take 3x this value.

Dependencies
------------

None.

Example Playbook
----------------

.. code-block:: yaml+jinja

    ---
    - hosts: firewalls

      vars:
        authcode: I1234567
        licensing_api_key: blahblahblah
        version: 10.0.2

      roles:
         - role: mrichardson03.panos.onboard

License
-------

ISC

Author Information
------------------

- Michael Richardson (@mrichardson03)
