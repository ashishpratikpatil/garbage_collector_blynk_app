from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def pick_up():
    import time
    print("BIN ON TOP")
    kit.servo[2].angle = 0
    
    time.sleep(2)
    
    #open
    kit.servo[0].angle = 180
    kit.servo[1].angle = 0
    time.sleep(2)
    
    kit.servo[2].angle = 150
    
    time.sleep(2)
    
    #close
    kit.servo[0].angle = 0
    kit.servo[1].angle = 180
    kit.servo[4].angle = 180
    
    time.sleep(2)
    
    kit.servo[2].angle = 0
    
    time.sleep(2)
    
    #open
    kit.servo[0].angle = 180
    kit.servo[1].angle = 0
    kit.servo[4].angle = 0
    
    
    
pick_up()