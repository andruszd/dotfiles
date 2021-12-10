mrichardson03.panos
===================

Ansible collection for automating configuration and maintenance tasks on Palo Alto Networks Next Generation Firewalls.

How is this different than paloaltonetworks.panos?
--------------------------------------------------

This collection is different than the official Palo Alto Networks collection in a number of key ways:

- **Direct XML API support.** All aspects of PAN-OS can be configured using the standard Ansible Jinja2 templating
  language.
- **Uses standard Ansible connection methods.** This collection is written using as an Ansible httpapi plugin. This
  allows for a number of enhancements, most notably persistent connections to the device.
- **Minimal dependencies.** Only uses ``requests`` and ``xmltodict``.

This collection is **not backwards compatible** with ``paloaltonetworks.panos``.  Certain module names have been reused,
but option names and/or defaults have been changed to reflect my own preferences.

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Contents

  getting_started

.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Reference

  modules
  roles
