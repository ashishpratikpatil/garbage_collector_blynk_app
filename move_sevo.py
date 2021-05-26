import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 60

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

#close
kit.servo[0].angle = 0
kit.servo[1].angle = 180


#open
kit.servo[0].angle = 180
kit.servo[1].angle = 0

import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.servo[4].angle = 180
time.sleep(2)
kit.servo[4].angle = 0