.. _panos_license_module:

panos_license
=============

Description
-----------

Applies a license authcode to a PAN-OS device.

The authcode should have been previously registered on the Palo Alto Networks support portal.

The PAN-OS device should have Internet access.



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

    
    - name: License the the device
      panos_license:
        authcode: "IBADCODE"
      register: result

    - debug:
        msg: 'Serial number is {{ result.serial }}'



Options
-------

``authcode``
^^^^^^^^^^^^
:description:
  Authcode to be applied.

:required: False
:type: str





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

``serial``
^^^^^^^^^^

:description:
  Serial number after authcode application.  Licensing VM-Series will generate a serial number.
:returned: success
:type: str

``licenses``
^^^^^^^^^^^^

:description:
  Licenses after authcode application.
:returned: success
:type: list
