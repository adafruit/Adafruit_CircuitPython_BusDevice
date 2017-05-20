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

    :param ~busio.SPI spi: The SPI bus the device is on
    :param ~microcontroller.Pin chip_select: The chip select pin
    :param int extra_clocks: The minimum number of clock cycles to cycle the bus after CS is high. (Used for SD cards.)

    .. note:: This class is **NOT** built into CircuitPython. See
      :ref:`here for install instructions <bus_device_installation>`.

    Example:

    .. code-block:: python

        import busio
        from board import *
        from adafruit_bus_device.spi_device import I2CDevice

        with busio.SPI(SCK, MOSI, MISO) as spi_bus:
            device = SPIDevice(spi_bus, D10)
            bytes_read = bytearray(4)
            with device as spi:
                spi_device.read(bytes_read)
            # A second transaction
            with device as spi:
                spi.write(bytes_read)
    """
    def __init__(self, spi, chip_select, baudrate=100000, polarity=0, phase=0, extra_clocks=0):
        self.spi = spi
        self.baudrate = baudrate
        self.polarity = polarity
        self.phase = phase
        self.extra_clocks = extra_clocks
        self.chip_select = chip_select
        self.chip_select.switch_to_output(value=True)

    def __enter__(self):
        while not self.spi.try_lock():
            pass
        self.spi.configure(baudrate=self.baudrate, polarity=self.polarity,
                           phase=self.phase)
        self.chip_select.value = False
        return self.spi

    def read_into(self, buf, **kwargs):
        """
        Read into ``buf`` from the device. The number of bytes read will be the
        length of ``buf``.

        If ``start`` or ``end`` is provided, then the buffer will be sliced
        as if ``buf[start:end]``. This will not cause an allocation like
        ``buf[start:end]`` will so it saves memory.

        :param bytearray buffer: buffer to write into
        :param int start: Index to start writing at
        :param int end: Index to write up to but not include
        """
        self.spi.readinto(buf, **kwargs)

    def write(self, buf, **kwargs):
            """
            Write the bytes from ``buffer`` to the device. Transmits a stop bit if
            ``stop`` is set.

            If ``start`` or ``end`` is provided, then the buffer will be sliced
            as if ``buffer[start:end]``. This will not cause an allocation like
            ``buffer[start:end]`` will so it saves memory.

            :param bytearray buffer: buffer containing the bytes to write
            :param int start: Index to start writing from
            :param int end: Index to read up to but not include
            :param bool stop: If true, output an I2C stop condition after the buffer is written
            """
            self.spi.write(buf, **kwargs)

    def __exit__(self, *exc):
        self.chip_select.value = True
        if self.extra_clocks > 0:
            buf = bytearray(1)
            buf[0] = 0xff
            clocks = self.extra_clocks // 8
            if self.extra_clocks % 8 != 0:
                clocks += 1
            for i in range(clocks):
                self.spi.write(buf)
        self.spi.unlock()
        return False
