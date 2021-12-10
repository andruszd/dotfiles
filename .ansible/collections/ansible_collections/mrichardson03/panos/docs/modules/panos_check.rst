.. _panos_check_module:

panos_check
===========

Description
-----------

Checks if the autocommit job on a PAN-OS device has completed, making the device ready for configuration.



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

    
    - name: Check if the device is ready
      panos_check:



Options
-------

``delay``
^^^^^^^^^
:description:
  Number of seconds to wait before starting checks.

:required: False
:type: int

``sleep``
^^^^^^^^^
:description:
  Number of seconds to wait in between checks.

:required: False
:type: int
:default: ``60``

``timeout``
^^^^^^^^^^^
:description:
  Maximum number of seconds to poll the PAN-OS device.

:required: False
:type: int
:default: ``600``





Return Values
-------------

``elapsed``
^^^^^^^^^^^

:description:
  Number of seconds until the device was ready.
:returned: success
:type: int

``msg``
^^^^^^^

:description:
  Status message on success or failure.
:returned: always
:type: str
