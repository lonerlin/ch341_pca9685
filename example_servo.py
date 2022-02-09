#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from pca9685 import PCA9685
pwm = PCA9685(0x41, debug=True)  # 对象初始化，指定IIC地址
pwm.setPWMFreq(50)               # 设置PWM的频率

for i in range(0, 180, 2):
    pwm.set_servo_angle(0, i)
    time.sleep(0.05)

for i in range(180, 0, -2):
    pwm.set_servo_angle(0, i)
    time.sleep(0.05)