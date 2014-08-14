import pyb
import sys
from pyb import I2C
from struct import unpack as unp
from MPU_6050 import MPU_6050
from array import array

mpu = MPU_6050(1,0)
light = pyb.LED(4)
switch = pyb.Switch()
mpu.config_accelerometer(2)

sens_x = 1000
sens_y = 500
sens_z = 17500
acc_x = array('i',[])
acc_y = array('i',[])
acc_z = array('i',[])
tim = array('i',[])
i = 0

while True:
    pyb.wfi()
    if switch():
        pyb.delay(200)
        vib_data = open('vib_data.csv', 'w')
        x, y, z = mpu.get_acc_values()
        while ((abs(x) < sens_x) or (abs(y) < sens_y) or (abs(z) < sens_z)):
            x, y, z = mpu.get_acc_values()
            pyb.delay(5)
        light.on()
        t0 = pyb.millis()
        while (i < 1000):
            x, y, z = mpu.get_acc_values()
            t1 = pyb.millis()
            acc_x.append(x)
            acc_y.append(y)
            acc_z.append(z)
            tim.append(t1-t0)
            pyb.delay(1)
            i += 1
        while i>0:
            i -= 1
            vib_data.write('{},{},{},{}\n'.format(tim[i],acc_x[i],acc_y[i],acc_z[i]))
        vib_data.close()
        light.off()
        pyb.delay(200)