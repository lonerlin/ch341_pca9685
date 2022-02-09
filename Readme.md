# ch341 iic 控制  pca9685   
### PCA9685是一个廉价又好用的东西，既可以控制舵机，又可以控制电机，还可以控制LED等等。   
### 通过pca9685类提供了舵机，电机，pwm输出等函数，方便通过电脑的USB口，使用ch341A或者ch41T连接pca9685来控制电机和舵机等设备。
### 驱动的安装：
*到官网下载驱动[驱动](http://www.wch.cn/downloads/CH341PAR_EXE.html)  
*双击ch341par.exe安装驱动
### 主要函数     
* setPWMFreq  设置PWM的频率，舵机为默认50，电机一般可以设置为1000
* digital_write  指定引脚输出高低电平,模仿Arduino的digitalWrite  
* analog_write  指定引脚输出高低电平,模仿Arduino的digitalWrite
* drive_motor   输入马达速度，驱动马达前进，此函数用于驱动那种需要两路PWM,两路数字信号的板，例如L298P
* drive_motor_2 输入马达速度，驱动马达前进,此函数用于驱动需要四路PWM驱动的板，如L298N
* drive_one_motor 控制一个马达（输出一个针脚的PWM，同analog_write)
* set_servo_angle 驱动舵机（0~180）  
 
### 详细的说明请参考pca9685类的注释.
### 下面是测试的图片，在PCA9685的0，1，2口接了三个led灯，让三个LED闪动。  
![实例图片](https://gitee.com/lonerlin/ch341_pca9685/raw/master/ch341T/example.jpg)   

```python
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
```




 