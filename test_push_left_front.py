from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

#sitting
while True :

    # 3 - inner
    # 2 - shoulder
    # 1 - elbow
    
    
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 135

    time.sleep(1)

    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 160
    # inner 
    kit.servo[5].angle = 133

    time.sleep(1)


    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 170
    # inner 
    kit.servo[5].angle = 131

    time.sleep(1)

    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130

    time.sleep(1)