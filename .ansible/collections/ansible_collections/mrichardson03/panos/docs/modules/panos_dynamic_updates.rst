.. _panos_dynamic_updates_module:

panos_dynamic_updates
=====================

Description
-----------

Installs the latest version of one or more PAN-OS dynamic updates.



.. contents::
   :local:
   :depth: 1

Notes
-----

:Authors:
  | Nathan Embery (@nembery)
  | Michael Richardson (@mrichardson03)
:Version Added: 1.0.0



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Install content updates
      panos_dynamic_updates:

    - name: Install latest WildFire update
      panos_dynamic_updates:
        content_type: ['wildfire']



Options
-------

``content_type``
^^^^^^^^^^^^^^^^
:description:
  The types of dynamic updates to install.

:required: False
:type: list
:default: ``['content']``
:choices: ``content``, ``anti-virus``, ``wildfire``





Return Values
-------------

``changed``
^^^^^^^^^^^

:description:
  A boolean value indicating if the task made any changes.
:returned: always
:type: bool

``content``
^^^^^^^^^^^

:description:
  Content version number, if installed.
:returned: if installed
:type: str

``anti-virus``
^^^^^^^^^^^^^^

:description:
  Anti-virus version number, if installed.
:returned: if installed
:type: str

``wildfire``
^^^^^^^^^^^^

:description:
  WildFire version number, if installed.
:returned: if installed
:type: str
