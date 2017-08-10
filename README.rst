Adafruit CircuitPython BusDevice
================================

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-busdevice/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/bus_device/en/latest/
    :alt: Documentation Status

.. image :: https://badges.gitter.im/adafruit/circuitpython.svg
    :target: https://gitter.im/adafruit/circuitpython?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
    :alt: Gitter

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

The `I2CDevice` and `SPIDevice` helper classes make managing transaction state
on a bus easy. For example, they manage locking the bus to prevent other
concurrent access. For SPI devices, it manages the chip select and protocol
changes such as mode. For I2C, it manages the device address.

.. _bus_device_installation:

Installation
-------------

This library is **NOT** built into CircuitPython to make it easy to update. To
install it either follow the directions below or :ref:`install the library
bundle <bundle_installation>`.

To install:

#. Download and unzip the `latest release zip <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/releases>`_.
#. Copy the unzipped ``adafruit_bus_device`` to the ``lib`` directory on the ``CIRCUITPY`` or ``MICROPYTHON`` drive.

API
---
.. toctree::
    :maxdepth: 3

    adafruit_bus_device/index
