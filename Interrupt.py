import pyb

blue = pyb.LED(4)
switch = pyb.Switch()

while True:
    
    pyb.wfi()
    
    if switch():
        pyb.delay(200)
        
        while not switch():
            blue.on()
                
        blue.off()
        pyb.delay(200)