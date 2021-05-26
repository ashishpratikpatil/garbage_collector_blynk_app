"""
[WRITE VIRTUAL PIN EXAMPLE] ========================================================================

Environment prepare:
In your Blynk App project:
  - add "Slider" widget,
  - bind it to Virtual Pin V4,
  - set values range 0-255
  - add "LED" widget and assign Virtual Pin V4 to it
  - Run the App (green triangle in the upper right corner).
  - define your auth token for current example and run it


This started program will periodically call and execute event handler "write_virtual_pin_handler".
In app you can move slider that will cause LED brightness change and will send virtual write event
to current running example. Handler will print pin number and it's updated value.

Schema:
====================================================================================================
          +-----------+                        +--------------+                    +--------------+
          |           |                        |              |                    |              |
          | blynk lib |                        | blynk server |                    |  blynk app   |
          |           |                        |  virtual pin |                    |              |
          |           |                        |              |                    |              |
          +-----+-----+                        +------+-------+                    +-------+------+
                |                                     |                                    |
                |                                     |  write event from "Slider" widget  |
                |                                     |                                    |
                |                                     +<-----------------------------------+
                |                                     |                                    |
                |                                     |                                    |
                |                                     |                                    |
                |                                     |                                    |
 event handler  |   write event to hw from server     |                                    |
(user function) |                                     |                                    |
     +-----------<------------------------------------+                                    |
     |          |                                     |                                    |
     |          |                                     |                                    |
     +--------->+                                     |                                    |
                |                                     |                                    |
                |                                     |                                    |
                |                                     |                                    |
                +                                     +                                    +
====================================================================================================
Additional blynk info you can find by examining such resources:

    Downloads, docs, tutorials:     https://blynk.io
    Sketch generator:               http://examples.blynk.cc
    Blynk community:                http://community.blynk.cc
    Social networks:                http://www.fb.com/blynkapp
                                    http://twitter.com/blynk_app
====================================================================================================

servo_left - 0
servo_right - 1
servo_mid - 2
servo_bin - 4
____________________________________BOARD PINS___________________________
Bin_sensor_1-31
Bin_sensor_2-33




"""







#bin_metal = 33
#bin_non_metal = 31
#GPIO.setup(bin_metal, GPIO.IN)
#GPIO.setup(bin_non_metal, GPIO.IN)



#time.sleep(2)

#from servod import default_servo


import blynklib

BLYNK_AUTH = "xtl_rZdEHnCGnJ2OWIsqwJBLGeriz6dl"

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

# register handler for virtual pin V4 write event
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35,GPIO.OUT)
    GPIO.setup(36,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    GPIO.setup(38,GPIO.OUT)
    print("car moving forward")
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(36,GPIO.LOW)
    GPIO.output(37,GPIO.HIGH)
    GPIO.output(38,GPIO.LOW)
    
    
# register handler for virtual pin V4 write event
@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35,GPIO.OUT)
    GPIO.setup(36,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    GPIO.setup(38,GPIO.OUT)
    print("car moving backward")
    GPIO.output(35,GPIO.LOW)
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(38,GPIO.HIGH)
    
    
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35,GPIO.OUT)
    GPIO.setup(36,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    GPIO.setup(38,GPIO.OUT)
    print("car moving right")
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(36,GPIO.LOW)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(38,GPIO.HIGH)
    
    
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35,GPIO.OUT)
    GPIO.setup(36,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    GPIO.setup(38,GPIO.OUT)
    print("car moving left")
    GPIO.output(35,GPIO.LOW)
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(37,GPIO.HIGH)
    GPIO.output(38,GPIO.LOW)
    
    
@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35,GPIO.OUT)
    GPIO.setup(36,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    GPIO.setup(38,GPIO.OUT)
    print("CAR STOPPED")
    GPIO.output(35,GPIO.HIGH)
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(37,GPIO.HIGH)
    GPIO.output(38,GPIO.HIGH)
    #GPIO.cleanup()
    
    
# register handler for virtual pin V4 write event
@blynk.handle_event('write V8')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    from adafruit_servokit import ServoKit
    kit = ServoKit(channels=16)

    kit.servo[0].angle = 180
    kit.servo[0].angle = 0


    kit.servo[1].angle = 0
    kit.servo[1].angle = 180
    blynk.notify('Garbage Collected')
    
@blynk.handle_event('write V11')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    from adafruit_servokit import ServoKit
    kit = ServoKit(channels=16)
    import time
    print("AUTO_PICKUP")
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
    
    time.sleep(2)
    
    kit.servo[2].angle = 0
    
    time.sleep(2)
    
    #open
    kit.servo[0].angle = 180
    kit.servo[1].angle = 0


# register handler for virtual pin V5 write event
@blynk.handle_event('write V30')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    from adafruit_servokit import ServoKit
    kit = ServoKit(channels=16)

    kit.servo[0].angle = 0
    kit.servo[0].angle = 180


    kit.servo[1].angle = 180
    kit.servo[1].angle = 0
    #blynk.notify('Garbage Disposed') # send push notification to Blynk App
"""   
@blynk.handle_event('read V10')
def read_virtual_pin_handler(pin):
    
    # your code goes here
    # ...
    # Example: get sensor value, perform calculations, etc
    from garbage_distance import cart_location
    bin_level = cart_location()
    sensor_data = bin_level
    critilcal_data_value = 15
    print("sensor data is", sensor_data)
        
    # send value to Virtual Pin and store it in Blynk Cloud 
    blynk.virtual_write(pin, sensor_data)
    
    # you can define if needed any other pin
    # example: blynk.virtual_write(24, sensor_data)
        
    # you can perform actions if value reaches a threshold (e.g. some critical value)
    if sensor_data < critilcal_data_value:
        
        #blynk.set_property(pin, 'color', '#FF0000') # set red color for the widget UI element 
        blynk.notify('NON-METALIC BIN FULL') # send push notification to Blynk App 
        #blynk.email(<youremail@email.com>, 'Email Subject', 'Email Body') # send email to specified address



"""
#GPIO.cleanup()
###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
