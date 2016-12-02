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

    :param SPI spi: The SPI bus the device is on
    :param ~microcontroller.Pin chip_select: The chip select pin

    Example::

        import nativeio
        from board import *
        from adafruit_bus_device.spi_device import I2CDevice

        with nativeio.SPI(SCK, MOSI, MISO) as spi:
            device = SPIDevice(spi, D10)
            bytes_read = bytearray(4)
            with device:
                device.read(bytes_read)
            # A second transaction
            with device:
                device.write(bytes_read)
    """
    def __init__(self, spi, chip_select, baudrate=100000, polarity=0, phase=0):
        self.spi = spi
        self.baudrate = baudrate
        self.polarity = polarity
        self.phase = phase
        self.chip_select = chip_select
        self.chip_select.switch_to_output(value=True)

    def read(self, buffer, **kwargs):
        """
        Read into ``buffer`` from the device. The number of bytes read will be the
        length of ``buffer``.

        If ``start`` or ``end`` is provided, then the buffer will be sliced
        as if ``buffer[start:end]``. This will not cause an allocation like
        ``buffer[start:end]`` will so it saves memory.

             :param bytearray buffer: buffer to write into
             :param int start: Index to start writing at
             :param int end: Index to write up to but not include
        """
        self.spi.read(buffer, **kwargs)

    def write(self, buffer, **kwargs):
        """
        Write the bytes from ``buffer`` to the device. Transmits a stop bit if
        ``stop`` is set.

        If ``start`` or ``end`` is provided, then the buffer will be sliced
        as if ``buffer[start:end]``. This will not cause an allocation like
        ``buffer[start:end]`` will so it saves memory.

          :param bytearray buffer: buffer containing the bytes to write
          :param int start: Index to start writing from
          :param int end: Index to read up to but not include
          :param bool stop: If true, output an I2C stop condition after the
                            buffer is written
        """
        self.spi.write(buffer, **kwargs)

    def __enter__(self):
        while not self.spi.try_lock():
            pass
        self.spi.configure(baudrate=self.baudrate, polarity=self.polarity,
                           phase=self.phase)
        self.chip_select.value = False
        return self

    def __exit__(self, *exc):
        self.chip_select.value = True
        self.spi.unlock()
        return False
