import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time 

bin_metal = 33
bin_non_metal = 31
GPIO.setup(bin_metal, GPIO.IN)
GPIO.setup(bin_non_metal, GPIO.IN)
while True:
    if  GPIO.input(bin_non_metal) == 1:
        print("entered")
        time.sleep(2)
    else:
        print("asdasdasdasdas")
        time.sleep(2)
        
