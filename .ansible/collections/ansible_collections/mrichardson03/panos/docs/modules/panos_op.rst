.. _panos_op_module:

panos_op
========

Description
-----------

Allows a user to execute an operational command on a PAN-OS device.



.. contents::
   :local:
   :depth: 1

Notes
-----

:Author:
  | Michael Richardson (@mrichardson03)
:Version Added: 1.0.0


.. note::
   - Check mode is NOT supported.

Examples
--------

.. code-block:: yaml+jinja

    
    - name: show system info
      panos_op:
        cmd: 'show system info'

    - name: show system info (as XML)
      panos_op:
        cmd: '<show><system><info/></system></show>'
        cmd_is_xml: true



Options
-------

``cmd``
^^^^^^^
:description:
  Operational command to run.

:required: True
:type: str

``cmd_is_xml``
^^^^^^^^^^^^^^
:description:
  If ``true``, treat the cmd option as a string already in XML format. If ``false``, attempt to convert it to XML before execution.

:required: False
:type: bool





Return Values
-------------

``changed``
^^^^^^^^^^^

:description:
  A boolean value indicating if the task had to make changes. Commands starting with ``diff`` and ``show`` are deemed to be safe, and will return ``false``.  All others will return ``true``.
:returned: always
:type: bool

``stdout``
^^^^^^^^^^

:description:
  Output of the command in native XML format.
:returned: always
:type: str

``stdout_dict``
^^^^^^^^^^^^^^^

:description:
  Output of 'cmd', converted into a dictionary format.
:returned: always
:type: dict
