Adafruit CircuitPython BusDevice
================================

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-busdevice/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/bus_device/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_BusDevice.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_BusDevice
    :alt: Build Status

The ``I2CDevice`` and ``SPIDevice`` helper classes make managing transaction state
on a bus easy. For example, they manage locking the bus to prevent other
concurrent access. For SPI devices, it manages the chip select and protocol
changes such as mode. For I2C, it manages the device address.

.. _bus_device_installation:

Installation
-------------

This library is **NOT** built into CircuitPython to make it easy to update. To
install it either follow the directions below or `install the library
bundle <bundle_installation>`_.

To install:

#. Download and unzip the `latest release zip <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/releases>`_.
#. Copy the unzipped ``adafruit_bus_device`` to the ``lib`` directory on the ``CIRCUITPY`` drive.

Usage Example
=============

See examples/read_register_i2c.py and examples/read_register_spi.py for examples of the module's usage.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
