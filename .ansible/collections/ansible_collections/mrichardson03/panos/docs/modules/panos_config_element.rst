.. _panos_config_element_module:

panos_config_element
====================

Description
-----------

Modifies an element in the PAN-OS configuration.



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

    
    - name: Configure login banner
      vars:
        banner_text: 'Authorized Personnel Only!'
      panos_config_element:
        xpath: '/config/devices/entry[@name="localhost.localdomain"]/deviceconfig/system'
        element: '<login-banner>{{ banner_text }}</login-banner>'

    - name: Create address object
      panos_config_element:
        xpath: /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address
        element: |
          <entry name="Test">
            <ip-netmask>1.1.1.1</ip-netmask>
          </entry>

    - name: Delete address object 'Test'
      panos_config_element:
        xpath: /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name='Test']
        state: 'absent'



Options
-------

``xpath``
^^^^^^^^^
:description:
  Location of the specified element in the XML configuration.

:required: True
:type: str

``element``
^^^^^^^^^^^
:description:
  The element, in XML format.

:required: False
:type: str

``edit``
^^^^^^^^
:description:
  If ``true``, replace any existing configuration at the specified location with the contents of *element*.

  If ``false``, merge the contents of *element* with any existing configuration at the specified location.

:required: False
:type: bool

``state``
^^^^^^^^^
:description:
  The state.

:required: False
:type: str
:default: ``present``
:choices: ``present``, ``absent``





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

``diff``
^^^^^^^^

:description:
  Information about the differences between the previous and current state.
  Contains 'before' and 'after' keys.
:returned: success, when needed
:type: dict
