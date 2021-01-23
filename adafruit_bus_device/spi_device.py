# SPDX-FileCopyrightText: 2016 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# pylint: disable=too-few-public-methods

"""
`adafruit_bus_device.spi_device` - SPI Bus Device
====================================================
"""
import time

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_BusDevice.git"


class SPIDevice:
    """
    Represents a single SPI device and manages locking the bus and the device
    address.

    :param ~busio.SPI spi: The SPI bus the device is on
    :param ~digitalio.DigitalInOut chip_select: The chip select pin object that implements the
        DigitalInOut API.
    :param int extra_clocks: The minimum number of clock cycles to cycle the bus after CS is high.
        (Used for SD cards.)
    :param int timeout: the amount of time (in seconds) to wait before timing out when trying
        to lock, defaults to 0.25 seconds. to disable timeout set 'timeout=None'.
        if the lock times out a RuntimeError will be raised.

    .. note:: This class is **NOT** built into CircuitPython. See
      :ref:`here for install instructions <bus_device_installation>`.

    Example:

    .. code-block:: python

        import busio
        import digitalio
        from board import *
        from adafruit_bus_device.spi_device import SPIDevice

        with busio.SPI(SCK, MOSI, MISO) as spi_bus:
            cs = digitalio.DigitalInOut(D10)
            device = SPIDevice(spi_bus, cs)
            bytes_read = bytearray(4)
            # The object assigned to spi in the with statements below
            # is the original spi_bus object. We are using the busio.SPI
            # operations busio.SPI.readinto() and busio.SPI.write().
            with device as spi:
                spi.readinto(bytes_read)
            # A second transaction
            with device as spi:
                spi.write(bytes_read)
    """

    def __init__(
        self,
        spi,
        chip_select=None,
        *,
        baudrate=100000,
        polarity=0,
        phase=0,
        extra_clocks=0,
        timeout=0.25,
    ):
        self.spi = spi
        self.baudrate = baudrate
        self.polarity = polarity
        self.phase = phase
        self.extra_clocks = extra_clocks
        self.chip_select = chip_select
        self.timeout = timeout
        if self.chip_select:
            self.chip_select.switch_to_output(value=True)

    def __enter__(self):
        # pylint: disable-msg=no-member
        if self.timeout is not None:
            lock_start_time = time.monotonic()
            while not self.spi.try_lock():
                if self.timeout > (time.monotonic() - lock_start_time):
                    raise RuntimeError("'SPIDevice' lock timed out")
        else:
            while not self.spi.try_lock():
                pass

        self.spi.configure(
            baudrate=self.baudrate, polarity=self.polarity, phase=self.phase
        )
        if self.chip_select is not None:
            self.chip_select.value = False
        return self.spi

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.chip_select is not None:
            self.chip_select.value = True
        if self.extra_clocks > 0:
            buf = bytearray(1)
            buf[0] = 0xFF
            clocks = self.extra_clocks // 8
            if self.extra_clocks % 8 != 0:
                clocks += 1
            for _ in range(clocks):
                self.spi.write(buf)
        self.spi.unlock()
        return False
