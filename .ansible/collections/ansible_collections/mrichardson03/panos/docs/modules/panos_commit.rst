.. _panos_commit_module:

panos_commit
============

Description
-----------

Commits changes to a PAN-OS device.



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

    
    - name: Commit firewall config
      panos_commit:

    - name: commit changes by specified admins to firewall
      panos_commit:
        admins: ['admin1','admin2']



Options
-------

``force``
^^^^^^^^^
:description:
  Perform a force commit.

:required: False
:type: bool

``exclude_device_and_network``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:description:
  Perform a partial commit, excluding device and network configurationa.

:required: False
:type: bool

``exclude_policy_and_objects``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
:description:
  Perform a partial commit, excluding policy and object configuration.

:required: False
:type: bool

``exclude_shared_objects``
^^^^^^^^^^^^^^^^^^^^^^^^^^
:description:
  Perform a partial commit, excluding shared object configuration.

:required: False
:type: bool

``description``
^^^^^^^^^^^^^^^
:description:
  Description to add to commit.

:required: False
:type: str

``admins``
^^^^^^^^^^
:description:
  Commit only the changes made by the specified administrators.

:required: False
:type: list

``sleep``
^^^^^^^^^
:description:
  Check commit status every X seconds.

:required: False
:type: int
:default: ``10``

``timeout``
^^^^^^^^^^^
:description:
  Generate an error if commit has not completed after X seconds.

:required: False
:type: int
:default: ``600``





Return Values
-------------

``changed``
^^^^^^^^^^^

:description:
  A boolean value indicating if the task had to make changes.
:returned: always
:type: bool

``msg``
^^^^^^^

:description:
  A string with an error message, if any.
:returned: failure, always
:type: str

``stdout``
^^^^^^^^^^

:description:
  output of the commit job as a JSON formatted string
:returned: always
:type: str

``stdout_xml``
^^^^^^^^^^^^^^

:description:
  output of the commit job as an XML formatted string
:returned: always
:type: str
