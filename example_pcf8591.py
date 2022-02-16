#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pcf8591 import PCF8591
import time

pcf8591 = PCF8591(0x48)     # 对象初始化，指定IIC地址(默认是0x48)

# 输出AOUT(板上D2 LED)
for i in range(0, 255):
    print("Output voltage value:{}".format(i))
    pcf8591.write(i)
    time.sleep(0.05)
pcf8591.write(0)

# 读取AIN0的值(可调电阻0-255)
while True:
    print("voltage value:{}".format(pcf8591.read(0)))
    time.sleep(0.1)
