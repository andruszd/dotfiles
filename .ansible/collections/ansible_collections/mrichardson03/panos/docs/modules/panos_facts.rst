.. _panos_facts_module:

panos_facts
===========

Description
-----------

Collects facts from PAN-OS devices.



.. contents::
   :local:
   :depth: 1

Notes
-----

:Author:
  | Michael Richardson (@mrichardson03)
:Version Added: 1.0.0



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Gather system facts
      panos_facts:






Return Values
-------------

``ansible_net_hostname``
^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Hostname of the local node.
:returned: always
:type: str

``ansible_net_serialnum``
^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Serial number of the local node.
:returned: always
:type: str

``ansible_net_model``
^^^^^^^^^^^^^^^^^^^^^

:description:
  Device model of the local node.
:returned: always
:type: str

``ansible_net_version``
^^^^^^^^^^^^^^^^^^^^^^^

:description:
  PanOS version of the local node.
:returned: always
:type: str

``ansible_net_uptime``
^^^^^^^^^^^^^^^^^^^^^^

:description:
  Uptime of the local node.
:returned: always
:type: str

``ansible_net_vm_uuid``
^^^^^^^^^^^^^^^^^^^^^^^

:description:
  UUID of the local node.
:returned: When the device model is "PA-VM"
:type: str

``ansible_net_vm_cpuid``
^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  CPU ID of the local node.
:returned: When the device model is "PA-VM"
:type: str

``ansible_net_vm_license``
^^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  PA-VM License of the local node.
:returned: When the device model is "PA-VM"
:type: str

``ansible_net_vm_cap_tier``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  VM Capacity Tier of the local node.
:returned: When the device model is "PA-VM"
:type: str

``ansible_net_vm_cpu_count``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Number of vCPU Cores of the local node.
:returned: When the device model is "PA-VM"
:type: str

``ansible_net_vm_memory``
^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Memory (in bytes) of the local node.
:returned: When the device model is "PA-VM"
:type: str

``ansible_net_vm_mode``
^^^^^^^^^^^^^^^^^^^^^^^

:description:
  VM Mode of the local node.
:returned: When the device model is "PA-VM"
:type: str

``ansible_net_full_commit_required``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Specifies whether full commit is required to apply changes.
:returned: always
:type: bool

``ansible_net_uncommitted_changes``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Specifies if commit is required to apply changes.
:returned: always
:type: bool

``ansible_net_multivsys``
^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Specifies whether multivsys mode is enabled on local node.
:returned: always
:type: str

``ansible_net_ha_enabled``
^^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Specifies if HA is enabled.
:returned: always
:type: bool

``ansible_net_ha_localmode``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Specifies the HA mode on local node.
:returned: When HA is enabled.
:type: str

``ansible_net_ha_localstate``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Specifies the HA state on local node.
:returned: When HA is enabled.
:type: str

``ansible_net_interfaces``
^^^^^^^^^^^^^^^^^^^^^^^^^^

:description:
  Network interface information.
:returned: always
:type: complex
