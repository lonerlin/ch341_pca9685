#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ch341T.ch341t_i2c import CH341TI2C
import time


class PCF8591:

    def __init__(self, address=0x48, dev_index=0):
        self.usb_iic = CH341TI2C(dev_index=dev_index)
        self.address = address

    def read(self, chn):
        """
        读取PCF8591的模拟输入（0-255）
        :param chn: 通道（0-3）
        :return: 输入电压转换为8位值
        """
        try:
            self.usb_iic.write(self.address, 0x48, 0x40 | chn)
            # self.usb_iic.write(self.address, 0x40 | chn)  # 01000000
            self.usb_iic.read(self.address, 0x40 | chn)
            # self.bus.read_byte(self.address, 0x40 | chn)  # dummy read to start conversion
        except Exception as e:
            print("Address: %s \n%s" % (self.address, e))
        return self.usb_iic.read(self.address, 0x40 | chn)

    def write(self, val):
        """
        输出电压值AOUT
        :param val: 8位值（0~255）
        :return: NULL
        """
        try:
            self.usb_iic.write(self.address, 0x40, int(val))
        except Exception as e:
            print("Error: Device address: 0x%2X \n%s" % (self.address, e))


if __name__ == '__main__':
    pcf8591 = PCF8591()
    while True:
        print("voltage value:{}".format(pcf8591.read(0)))
        time.sleep(0.1)
