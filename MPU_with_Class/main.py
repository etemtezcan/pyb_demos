import pyb
import sys
from pyb import I2C
from struct import unpack as unp
from MPU_6050 import MPU_6050
from array import array

mpu = MPU_6050(1,1)
light = pyb.LED(4)
switch = pyb.Switch()
mpu.config_accelerometer(2)
mpu.config_gyroscope(250)

rtc = pyb.RTC()
rtc.datetime((2014, 8, 14, 4, 11, 25, 0 , 0))
a = rtc.datetime()
name = '{}_{}_{}_{}_{}.csv'.format(a[0],a[1],a[2],a[4],a[5])

eps_x = 250
eps_y = 200
eps_z = 1500
norm_x = 450
norm_y = -170
norm_z = 16000
acc_x = array('i',[])
acc_y = array('i',[])
acc_z = array('i',[])
gyro_x = array('i',[])
gyro_y = array('i',[])
gyro_z = array('i',[])
tim = array('i',[])
i = 0

while True:
    pyb.wfi()
    if switch():
        pyb.delay(200)
        vib_data = open(name, 'w')
        ax, ay, az = mpu.get_acc_values()
        while ((abs(norm_x - ax) < eps_x) or (abs(norm_y - ay) < eps_y) or (abs(norm_z - az) < eps_z)):
            ax, ay, az = mpu.get_acc_values()
            pyb.delay(5)
        light.on()
        t0 = pyb.millis()
        while (i < 1000):
            ax, ay, az = mpu.get_acc_values()
            gx, gy, gz = mpu.get_gyro_values()
            t1 = pyb.millis()
            acc_x.append(ax)
            acc_y.append(ay)
            acc_z.append(az)
            gyro_x.append(gx)
            gyro_y.append(gy)
            gyro_z.append(gz)
            tim.append(t1-t0)
            pyb.delay(1)
            i += 1
        while i>0:
            i -= 1
            a_x = acc_x[i]/16384
            a_y = acc_y[i]/16384
            a_z = acc_z[i]/16384
            g_x = (gyro_x[i]*250)/32768
            g_y = (gyro_y[i]*250)/32768
            g_z = (gyro_z[i]*250)/32768
            vib_data.write('{},{},{},{},{},{},{}\n'.format(tim[i],a_x,a_y,a_z,g_x,g_y,g_z))
        vib_data.close()
        light.off()
        pyb.delay(200)