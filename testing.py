from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)


#sitting
for _ in range(1):

   

    # ----------------------------- POINT 5 (Right front and left back lift up )
    # right front

    # LEFT FRONT
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130

    # RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 0
    # ----------------------------- 

