.. _panos_snippet_group_module:

panos_snippet_group
===================

Description
-----------

Sets config elements from a YAML definition file.



.. contents::
   :local:
   :depth: 1

Notes
-----

:Author:
  | Nathan Embery (@nembery)
:Version Added: 1.0.0



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Custom BGP Configuration
      vars:
        asn: 64512
        peer_asn: 64515
      panos_snippet_group:
        src: bgp.yaml




Options
-------

``src``
^^^^^^^
:description:
  The relative path to a snippet definition file to load

:required: True
:type: str





Return Values
-------------

``snippets``
^^^^^^^^^^^^

:description:
  List of differences found from existing running configuration and requested snippets
:returned: success
:type: str
