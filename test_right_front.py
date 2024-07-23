from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

#sitting
while True :

    # 3 - inner
    # 2 - shoulder
    # 1 - elbow


    # ----------------------------- POINT 1

    # right front
    # shoulder
    kit.servo[9].angle = 30
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)
    # ----------------------------- 


    # ----------------------------- POINT 2

    # right front
    # shoulder
    kit.servo[9].angle = 30
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 70

    time.sleep(1)
    # ----------------------------- 

    # ----------------------------- POINT 3

    # right front
    # shoulder
    kit.servo[9].angle = 70
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 160

    time.sleep(1)
    # ----------------------------- 



    # ----------------------------- POINT 4

    # right front
    # shoulder
    kit.servo[9].angle = 10
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)
    # ----------------------------- 
 