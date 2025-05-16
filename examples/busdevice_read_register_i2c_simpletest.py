# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio

from adafruit_bus_device.i2c_device import I2CDevice

DEVICE_ADDRESS = 0x68  # device address of DS3231 board
A_DEVICE_REGISTER = 0x0E  # device id register on the DS3231 board

# The follow is for I2C communications
comm_port = busio.I2C(board.SCL, board.SDA)
device = I2CDevice(comm_port, DEVICE_ADDRESS)

with device as bus_device:
    bus_device.write(bytes([A_DEVICE_REGISTER]))
    result = bytearray(1)
    bus_device.readinto(result)

print("".join(f"{x:02x}" for x in result))
