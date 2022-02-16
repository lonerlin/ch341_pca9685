# ch341 iic ����  pca9685��pcf8591  
### PCA9685��һ�������ֺ��õĶ������ȿ��Կ��ƶ�����ֿ��Կ��Ƶ���������Կ���LED�ȵȡ�   
### ͨ��pca9685���ṩ�˶���������pwm����Ⱥ���������ͨ�����Ե�USB�ڣ�ʹ��ch341A����ch41T����pca9685�����Ƶ���Ͷ�����豸��
### �����İ�װ��
* ����������ch341T����������[��������](http://www.wch.cn/downloads/CH341PAR_EXE.html)  
* ˫��ch341par.exe��װ����
* ch341T���ߵ�IICģʽ   

### ��Ҫ����     
* setPWMFreq  ����PWM��Ƶ�ʣ����ΪĬ��50�����һ���������Ϊ1000
* digital_write  ָ����������ߵ͵�ƽ,ģ��Arduino��digitalWrite  
* analog_write  ָ���������PWM,ģ��Arduino��analog_Write
* drive_motor   ��������ٶȣ��������ǰ�����˺�����������������Ҫ��·PWM,��·�����źŵİ壬����L298P
* drive_motor_2 ��������ٶȣ��������ǰ��,�˺�������������Ҫ��·PWM�����İ壬��L298N
* drive_one_motor ����һ�������һ����ŵ�PWM��ͬanalog_write)
* set_servo_angle ���������0~180��  
 
### ��ϸ��˵����ο�pca9685���ע��.
### �����ǲ��Ե�ͼƬ����PCA9685��0��1��2�ڽ�������led�ƣ�������LED������  
![ʵ��ͼƬ](https://gitee.com/lonerlin/ch341_pca9685/raw/master/ch341T/example.jpg)   

```python
import time
from pca9685 import PCA9685
pwm = PCA9685(0x40, debug=True)  # �����ʼ����ָ��IIC��ַ
pwm.setPWMFreq(50)               # ����PWM��Ƶ��
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

### pcf8591����4·8λ��ģ�����룬1·ģ����������pca9685ʹ�ã������ֲ�pca9685ֻ����������������ȱ��   
```python
from pcf8591 import PCF8591
import time

pcf8591 = PCF8591(0x48)   # �����ʼ����ָ��IIC��ַ
while True:
    print("voltage value:{}".format(pcf8591.read(0)))  # ��ȡAIN0��ֵ��0-255��
    time.sleep(0.1)
```



 