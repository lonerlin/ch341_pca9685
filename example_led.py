#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from pca9685 import PCA9685
pwm = PCA9685(0x40, debug=True)  # 对象初始化，指定IIC地址
pwm.setPWMFreq(50)               # 设置PWM的频率
print("start the control")
r = 0
g = 0
b = 1
while True:
    r = not r
    g = not g
    b = not b
    pwm.digital_write(0, r)
    pwm.digital_write(1, g)
    pwm.digital_write(2, b)
    time.sleep(1)