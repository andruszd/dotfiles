.. _panos_software_module:

panos_software
==============

Description
-----------

Installs a PAN-OS software release.



.. contents::
   :local:
   :depth: 1

Notes
-----

:Author:
  | Michael Richardson (@mrichardson03)
:Version Added: 1.0.0


.. note::
   - Check mode is supported.

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Install PAN-OS 8.1.6 and restart
      panos_software:
        version: '8.1.6'
        restart: true

    - name: Download PAN-OS 9.0.0 base image only
      panos_software:
        version: '9.0.0'
        install: false
        restart: false

    - name: Download PAN-OS 9.0.1 and sync to HA peer
      panos_software:
        version: '9.0.1'
        sync_to_peer: true
        install: false
        restart: false



Options
-------

``version``
^^^^^^^^^^^
:description:
  Desired PAN-OS release for target device.  If this version is in the next PAN-OS release, the base image for that release will be downloaded as well.

  For example, if the PAN-OS device is currently running 9.1.0, and 'version' is set to 10.0.2, the 10.0.0 base image will be downloaded and the 10.0.2 image will be downloaded and installed.

:required: True
:type: str

``sync_to_peer``
^^^^^^^^^^^^^^^^
:description:
  If device is a member of a HA pair, perform actions on the peer device as well.  Only used when downloading software, installation must be performed on both devices.

:required: False
:type: bool

``download``
^^^^^^^^^^^^
:description:
  Download PAN-OS version to the device.

:required: False
:type: bool
:default: ``True``

``install``
^^^^^^^^^^^
:description:
  Perform installation of the PAN-OS version on the device.

:required: False
:type: bool
:default: ``True``

``restart``
^^^^^^^^^^^
:description:
  Restart device after installing desired version.  Use in conjunction with panos_check to determine when firewall is ready again.

:required: False
:type: bool

``timeout``
^^^^^^^^^^^
:description:
  Maximum amount of time (in seconds) each software download or installation job performed by this module is allowed to run before error.

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
