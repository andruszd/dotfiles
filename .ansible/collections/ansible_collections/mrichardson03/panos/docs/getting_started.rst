Getting Started
===============

Install the collection
----------------------

This collection is written for Python 3.8, which is the version used in the default Ansible AWX virtual environment.
Newer versions of Python will likely work, but are not tested.

Install this collection using the Ansible Galaxy CLI, and install the required Python libraries:

.. code-block:: bash

  ansible-galaxy collection install mrichardson03.panos
  pip3 install --user xmltodict requests

Configure your inventory
------------------------

The modules in this collection use the ``httpapi`` connection type, so all of the
`httpapi connection options`_ can be used.

.. _httpapi connection options: https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/httpapi_connection.html

.. code-block:: ini

  firewall        ansible_host=192.168.55.10

  [all:vars]
  ansible_user=admin
  ansible_password=P4loalto!

  ansible_network_os=mrichardson03.panos.panos
  ansible_connection=httpapi
  ansible_httpapi_use_ssl=True
  ansible_httpapi_validate_certs=False

Modify configuration
--------------------

Manipulating configuration is performed with :ref:`panos_config_element_module`.

This module writes a piece of configuration (*element*) to a specific location (*xpath*) in the PAN-OS config.

.. code-block:: yaml

  ---
  - hosts: firewall

    collections:
      - mrichardson03.panos

    tasks:
      - name: Create vulnerability protection profile
        panos_config_element:
          xpath: "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/profiles/vulnerability"
          element: |
            <entry name="Outbound-Vuln-Profile">
              <rules>
                <entry name="Block-Critical-High-Medium">
                  <action>
                    <reset-both/>
                  </action>
                  <vendor-id>
                    <member>any</member>
                  </vendor-id>
                  <severity>
                    <member>critical</member>
                    <member>high</member>
                    <member>medium</member>
                  </severity>
                  <cve>
                    <member>any</member>
                  </cve>
                  <threat-name>any</threat-name>
                  <host>any</host>
                  <category>any</category>
                  <packet-capture>single-packet</packet-capture>
                </entry>
              </rules>
            </entry>

Ansible uses `Jinja`_ for templating, which allows for features like variable replacement and looping to be used.  This
makes it easy to reuse portions of configuration.

.. _Jinja: https://jinja.palletsprojects.com/en/3.0.x/templates/

.. code-block:: yaml+jinja

  - name: Jinja template example
    panos_config_element:
      xpath: "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address"
      element: |
        {% for object in address_objects %}
          <entry name="{{ object.name }}">
            <{{ object.type | default("ip-netmask") }}>{{ object.value }}</{{ object.type | default("ip-netmask") }}>
        {% if 'description' in object %}
            <description>{{ object.description }}</description>
        {% endif %}
          </entry>
        {% endfor %}
    vars:
      address_objects:
        - name: "web-srv"
          value: "192.168.45.5"
        - name: "db-srv"
          value: "192.168.35.5"
          type: "ip-netmask"
          description: "database server"
        - name: "fqdn-test"
          type: "fqdn"
          value: "foo.bar.baz"

In this example, a list of dictionaries named *address_objects* is looped over.  Each dictionary in this list describes
the elements of an individual address object.  Once the Jinja template processing is complete, it will result in the
following call:

.. code-block:: yaml+jinja

  - name: Jinja template example (expanded)
    panos_config_element:
      xpath: "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address"
      element: |
        <entry name="web-srv">
          <ip-netmask>192.168.45.5</ip-netmask>
        </entry>
        <entry name="db-srv">
          <ip-netmask>192.168.35.5</ip-netmask>
          <description>database server</description>
        </entry>
        <entry name="fqdn-test">
          <fqdn>foo.bar.baz</fqdn>
        </entry>

This is especially powerful, because this performs a bulk write of these three objects to PAN-OS as one API operation.
PAN-OS has a maximum API request size of 5MB, so thousands of config elements can be written at once, provided the xpath
is the same.

Ansible also allows for storing templates in an external file and looking them up with the `template lookup filter`_.
This makes it easy to reuse XML config elements across playbooks, or they can be stored in `roles`_ for even more
flexibility.

.. _template lookup filter: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_lookup.html
.. _roles: https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html

.. code-block:: yaml+jinja

  - name: Create NAT rules
    panos_config_element:
      xpath: /config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/nat/rules
      element: "{{ lookup('template', 'nat_rules.xml.j2') }}"

See the :ref:`firewall_role` role for an example of how this can be used.
