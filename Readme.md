# ch341 iic ����  pca9685   
### PCA9685��һ�������ֺ��õĶ������ȿ��Կ��ƶ�����ֿ��Կ��Ƶ���������Կ���LED�ȵȡ�   
### ͨ��ʹ��pca9685���ṩ�˶���������pwm������Ⱥ���������ͨ�����Ե�USB�ڣ�ʹ��ch341A����ch41T�����Ƶ���Ͷ�����豸��
### ��ϸ��˵����ο����ע��
### �����ǲ��Ե�ͼƬ����PCA9685��0��1��2�ڽ�������led�ƣ����ϸ�LED������  
![ʵ��ͼƬ](https://gitee.com/lonerlin/ch341_pca9685/raw/master/ch341T/example.jpg)   

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




 