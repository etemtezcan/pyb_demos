# main.py -- put your code here!

import pyb
from pyb import I2C
from struct import unpack as unp

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
            x = unp('>h', i2c.mem_read(2, 0x68, 0x3B))[0]
            y = unp('>h', i2c.mem_read(2, 0x68, 0x3D))[0]
            z = unp('>h', i2c.mem_read(2, 0x68, 0x3F))[0]
            log.write('{},{},{}\n'.format(x,y,z))
        log.close()
        light.off()
        pyb.delay(200)