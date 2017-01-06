Adafruit CircuitPython BusDevice
==============================

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-bus_device/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/bus_device/en/latest/
    :alt: Documentation Status

The `I2CDevice` and `SPIDevice` helper classes make managing transaction state
on a bus easy. For example, they manage locking the bus to prevent other
concurrent access. For SPI devices, it manages the chip select and protocol
changes such as mode. For I2C, it manages the device address.

API
---
.. toctree::
    :maxdepth: 3

    adafruit_bus_device/index
