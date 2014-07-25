# main.py -- put your code here!
import pyb
import sys
sys.path.append('1:/') #to find modules in sdCard 
from pyb import I2C
from struct import unpack as unp
from MPU_6050 import MPU_6050

mpu = MPU_6050(1,0)
light = pyb.LED(4)
switch = pyb.Switch()
mpu.config_accelerometer(2)

while True:
    if switch():
        pyb.delay(200) #wait for button press
        light.on() #indicate that the logging started
        try:
            vib_data = open('1:/vib_data.csv', 'w') #0:internal, 1:sdCard
        except IOError:
            print('An error occurred trying to open the file.')
        while not switch(): #do until the button is pressed again
            x, y, z = mpu.get_acc_values()
            vib_data.write('{},{},{}\n'.format(x,y,z)) #write the acquired data to the logging file
        vib_data.close() #after the button is pressed again, close the logging file
        light.off() #switch off the light in order to indicate that the logging has stopped
        pyb.delay(200) #wait for button press
        