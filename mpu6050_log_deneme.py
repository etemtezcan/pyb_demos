# main.py -- put your code here!

import pyb
from pyb import I2C

light = pyb.LED(4)
switch = pyb.Switch()

while True:
    if switch():
        pyb.delay(200)
        light.on()
        log = open('0:/log.csv', 'w')
        i2c = I2C(2, I2C.MASTER)
        i2c.mem_write(0, 0x68, 0x6B)
        while not switch():
            x_h = i2c.mem_read(1, 0x68, 0x3B)
            x_l = i2c.mem_read(1, 0x68, 0x3C)
            y_h = i2c.mem_read(1, 0x68, 0x3D)
            y_l = i2c.mem_read(1, 0x68, 0x3E)
            z_h = i2c.mem_read(1, 0x68, 0x3F)
            z_l = i2c.mem_read(1, 0x68, 0x40)
				#x = ((x_h*256) | x_l)
				#y = ((y_h*256) | y_l)
				#z = ((z_h*256) | z_l)
        log.write('{},{},{},{},{},{}\n'.format(x_h,y_h,z_h,x_l,y_l,z_l))
        log.close()
        light.off()
        pyb.delay(200)