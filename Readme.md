# ch341 iic 控制  pca9685   
### PCA9685是一个廉价又好用的东西，既可以控制舵机，又可以控制电机，还可以控制LED等等。   
### 通过使用pca9685类提供了舵机，电机，pwm，输出等函数，方便通过电脑的USB口，使用ch341A或者ch41T来控制电机和舵机等设备。
### 详细的说明请参考类的注释
### 下面是测试的图片，在PCA9685的0，1，2口接了三个led灯，让上个LED闪动。  
![实例图片](https://gitee.com/lonerlin/ch341_pca9685/raw/master/ch341T/example.jpg)   

```python
import time
from pca9685 import PCA9685
pwm = PCA9685(0x40, debug=True)
pwm.setPWMFreq(50)
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




 