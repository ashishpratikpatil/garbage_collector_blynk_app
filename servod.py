#Default Position

def default_servo():
    from adafruit_servokit import ServoKit
    kit = ServoKit(channels=16)

    kit.servo[2].angle = 0 # BIN on top

    kit.servo[0].angle = 180
    kit.servo[1].angle = 0
