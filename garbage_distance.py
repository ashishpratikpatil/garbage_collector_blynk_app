

def cart_location():
    import RPi.GPIO as GPIO
    import time


    GPIO.setmode(GPIO.BOARD)

    TRIG = 33
    ECHO = 31
    global distance

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setwarnings(False)

    GPIO.output(TRIG, False)
    print ("Calibrating for 2 seconds.....")
    time.sleep(2)
    print("calibration complete")

    #print ("Place the object......")

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    pulse_start = 0
    pulse_end = 0

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    global pulse_duration 
    pulse_duration = pulse_end - pulse_start
    global distance
    distance = pulse_duration * 17150

    distance = round(distance+1.15, 2)
      
           #if distance<=200 and distance>=5:
               
    print ("cart location is at:",distance,"cm")

    time.sleep(1)
    GPIO.cleanup()
    return distance
cart_location()

