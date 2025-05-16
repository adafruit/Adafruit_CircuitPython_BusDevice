# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import digitalio

from adafruit_bus_device.spi_device import SPIDevice

A_DEVICE_REGISTER = 0xD0  # device id register on the BMP280 board

# The follow is for SPI communications
cs = digitalio.DigitalInOut(board.A2)
comm_port = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
device = SPIDevice(comm_port, cs)

with device as bus_device:
    bus_device.write(bytes([A_DEVICE_REGISTER]))
    result = bytearray(1)
    bus_device.readinto(result)

print("".join(f"{x:02x}" for x in result))
