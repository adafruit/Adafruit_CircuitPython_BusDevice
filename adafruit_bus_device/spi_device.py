# The MIT License (MIT)
#
# Copyright (c) 2016 Scott Shawcroft for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

class SPIDevice:
    """
    Represents a single SPI device and manages locking the bus and the device
    address.

    :param ~nativeio.SPI spi: The SPI bus the device is on
    :param ~microcontroller.Pin chip_select: The chip select pin

    .. note:: This class is **NOT** built into CircuitPython. See
      :ref:`here for install instructions <bus_device_installation>`.

    Example:

    .. code-block:: python

        import nativeio
        from board import *
        from adafruit_bus_device.spi_device import I2CDevice

        with nativeio.SPI(SCK, MOSI, MISO) as spi_bus:
            device = SPIDevice(spi_bus, D10)
            bytes_read = bytearray(4)
            with device as spi:
                spi_device.read(bytes_read)
            # A second transaction
            with device as spi:
                spi.write(bytes_read)
    """
    def __init__(self, spi, chip_select, baudrate=100000, polarity=0, phase=0):
        self.spi = spi
        self.baudrate = baudrate
        self.polarity = polarity
        self.phase = phase
        self.chip_select = chip_select
        self.chip_select.switch_to_output(value=True)

    def __enter__(self):
        while not self.spi.try_lock():
            pass
        self.spi.configure(baudrate=self.baudrate, polarity=self.polarity,
                           phase=self.phase)
        self.chip_select.value = False
        return self.spi

    def __exit__(self, *exc):
        self.chip_select.value = True
        self.spi.unlock()
        return False
