#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ctypes
import os


class CH341TI2C:

    # CH341T IIC通信，在32位和64位python测试成功，只需根据环境指定64位，或32位的DLL路径即可使用。

    def __init__(self, dll_path="./ch341T/CH341DLLA64.dll", dev_index=0):
        """
        初始化CH341T的控制模块，根据参数，测试模块是否可用
        :param dll_path: ch341T的dll文件路径
        :param dev_index: 指定CH341设备序号,0对应第一个设备
        """

        self.dll = ctypes.windll.LoadLibrary(dll_path)
        self.usb_id = dev_index
        self.i2c_speed = 2
        self.check_device()

    def check_device(self):
        """
        尝试打开设备
        """
        if self.dll.CH341OpenDevice(self.usb_id) > 0:
            print("Open USB CH341Dev Index=", self.usb_id, "ok!!!!!!!")
            self.dll.CH341CloseDevice(self.usb_id) > 0
        else:
            print("Error!!! USB CH341 Open Failed!")

    def set_i2c_speed(self, speed=2):
        """
        设置iic口流模式（用于指定速度）
            位1-位0: I2C接口速度/SCL频率, 00=低速/20KHz,01=标准/100KHz(默认值),10=快速/400KHz,11=高速/750KHz
            位2:     SPI的I/O数/IO引脚, 0=单入单出(D3时钟/D5出/D7入)(默认值),1=双入双出(D3时钟/D5出D4出/D7入D6入)
            位7:     SPI字节中的位顺序, 0=低位在前, 1=高位在前
            其它保留,必须为0
        :param speed:速度值
        :return:设置成功返回1，失败返回-1
        """
        self.i2c_speed = speed
        if self.dll.CH341OpenDevice(self.usb_id) > 0:
            if self.dll.CH341SetStream(self.usb_id, 0x80 + speed) > 0:
                print("set I2C speed to ", speed, "(3=750Khz, 2=400k, 1=100k, 0=20k")
                return 1
            else:
                print("set I2C speed to ", speed, "Fail ,please check your CH341 Device !!")
                return -1
        else:
            print("Error!!! USB CH341 Open Failed!")
            return -1

    def ch341_swi2c(self, i2c_addr7b, reg_addr, wdata):
        """
        向I2C接口写入一个字节数据
        :param i2c_addr7b: 低7位指定I2C设备地址
        :param reg_addr: 指定数据单元的地址
        :param wdata:  待写入的字节数据
        :return:
        """
        return self.dll.CH341WriteI2C(self.usb_id, i2c_addr7b & 0xff, reg_addr & 0xff, wdata & 0xff)

    def ch341_sri2c(self, i2c_addr7b, reg_addr):
        """
        从I2C接口读取一个字节数据
        :param i2c_addr7b: 低7位指定I2C设备地址
        :param reg_addr: 指定数据单元的地址
        :return: 读取的8位值
        """
        read_data = (ctypes.c_uint8 * 1)()
        if self.dll.CH341ReadI2C(self.usb_id, i2c_addr7b & 0xff, reg_addr & 0xff, read_data) > 0:
            return read_data[0] & 0xff
        else:
            return -1

    def read(self, i2c_addr, reg_addr):
        """
        打开设备，读取数据，是对ch341_sri2c的进一步封装
        :param i2c_addr: 低7位指定I2C设备地址
        :param reg_addr: 指定数据单元的地址
        :return: 读取的8位值
        """
        if self.dll.CH341OpenDevice(self.usb_id) > 0:
            result = self.ch341_sri2c(i2c_addr, reg_addr)
            self.dll.CH341CloseDevice(self.usb_id)
            return result
        else:
            print("USB CH341 Open Failed!")
            return 0

    def write(self, i2c_addr, reg_addr, dat):
        """
        打开设备，写入数据，是对ch341_swi2c的进一步封装
        :param i2c_addr: 低7位指定I2C设备地址
        :param reg_addr: 指定数据单元的地址
        :param dat: 写入的数据
        :return: 写入是否成功，成功返回1
        """
        if self.dll.CH341OpenDevice(self.usb_id) > 0:
            result = self.ch341_swi2c(i2c_addr, reg_addr, dat)
            self.dll.CH341CloseDevice(self.usb_id)
            return result
        else:
            print("USB CH341 Open Failed!")
