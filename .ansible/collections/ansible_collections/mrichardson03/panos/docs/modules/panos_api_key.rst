.. _panos_api_key_module:

panos_api_key
=============

Description
-----------

Generates an API key for a specified user.



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

    
    - name: Generate API key
      panos_api_key:
      register: auth

    - debug:
        msg: '{{ auth.api_key }}'






Return Values
-------------

``api_key``
^^^^^^^^^^^

:description:
  Generated API key
:returned: success
:type: str
