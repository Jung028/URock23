from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

#sitting
while True :

    # 3 - inner
    # 2 - shoulder
    # 1 - elbow


    # -------------------------- POINT 1 (starting point)
    # left front
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 135

        # shoulder
    kit.servo[9].angle = 30
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    time.sleep(0.2)

    # -------------------------- 

    # -------------------------- POINT 2 
    # elbow
    kit.servo[3].angle = 140
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 133

        # shoulder
    kit.servo[9].angle = 20
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 120


    time.sleep(0.2)
    # -------------------------- 


    # -------------------------- POINT 3

    # elbow
    kit.servo[3].angle = 70
    # shoulder
    kit.servo[4].angle = 120
    # inner 
    kit.servo[5].angle = 133

        # shoulder
    kit.servo[9].angle = 10
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 130


    time.sleep(0.2)
    # -------------------------- 


    # -------------------------- POINT 4 (Push Back)

    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130

        # shoulder
    kit.servo[9].angle = 0
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 160

    time.sleep(0.2)
    # -------------------------- 

    # right front
    # shoulder
    kit.servo[9].angle = 30
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 70

    time.sleep(0.2)

        # right front
    # shoulder
    kit.servo[9].angle = 70
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 160

    time.sleep(0.1)
    # ----------------------------- 

