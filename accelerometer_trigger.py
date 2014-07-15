import pyb

accel = pyb.Accel()
light = pyb.LED(4)
switch = pyb.Switch()
SENSITIVITY = 3

while True:
		t = pyb.millis()
		x = accel.x()
		if abs(x) > SENSITIVITY:
				pyb.delay(200)
				light.on()
				log = open('0:/log.csv', 'w')
				while not switch():
						t = pyb.millis()
						x, y, z = accel.filtered_xyz()
						log.write('{},{},{},{}\n'.format(t,x,y,z))
				log.close()
				light.off()
				pyb.delay(200)
		else:
				pyb.delay(200)