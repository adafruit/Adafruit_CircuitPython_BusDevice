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

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-busdevice --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.

