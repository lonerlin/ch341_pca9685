#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from pca9685 import PCA9685
i2c = PCA9685(0x40, debug=True)  # 对象初始化，指定IIC地址
i2c.setPWMFreq(1000)               # 设置PWM的频率
print("start")
time.sleep(1)      # 等待一秒

print("马达开始转动：")
time.sleep(1)

print("两个马达正向转动：")
for i in range(20, 255, 5):
    i2c.drive_motor(i, i)
    time.sleep(0.3)

print("右马达正向转动，左马达停止：")

for i in range(20, 255, 5):
    i2c.drive_motor(0, i)
    time.sleep(0.3)

print("左马达正向转动，右马达停止：")
for i in range(20, 255, 5):
    i2c.drive_motor(i, 0)
    time.sleep(0.3)

print("两个马达反向转动：")
for i in range(20, 255, 5):
    i2c.drive_motor(-i, -i)
    time.sleep(0.3)

print("马达停止")
i2c.drive_motor(0, 0)