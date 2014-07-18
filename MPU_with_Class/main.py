# main.py -- put your code here!
from MPU_6050 import MPU_6050
import pyb
from pyb import I2C
from struct import unpack as unp

mpu = MPU_6050(1,0)
light = pyb.LED(4)
switch = pyb.Switch()
mpu.config_accelerometer(2)

while True:
    if switch():
        pyb.delay(200) #wait for button press
        light.on() #indicate that the logging started
        vib_data = open('0:/vib_data.csv', 'w') #open the logging file
        while not switch(): #do until the button is pressed again
            x, y, z = mpu.get_acc_values()
            vib_data.write('{},{},{}\n'.format(x,y,z)) #write the acquired data to the logging file
        vib_data.close() #after the button is pressed again, close the logging file
        light.off() #switch off the light in order to indicate that the logging has stopped
        pyb.delay(200) #wait for button press