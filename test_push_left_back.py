from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

#sitting
while True :

    # 3 - inner
    # 2 - shoulder
    # 1 - elbow




    # ----------------------------- POINT 1 (Starting)
 
    # elbow
    kit.servo[0].angle = 130
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 160
    time.sleep(1)
    # ----------------------------- 

     # ----------------------------- POINT 1 (Starting)
 
    # elbow
    kit.servo[0].angle = 110
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 165
    time.sleep(1)
    # ----------------------------- 


     # ----------------------------- POINT 1 (Starting)
 
    # elbow
    kit.servo[0].angle = 90
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 175
    time.sleep(1)
    # ----------------------------- 
 
    # ----------------------------- POINT 1 (Starting)
 
    # elbow
    kit.servo[0].angle = 80
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 180
    time.sleep(1)
    # ----------------------------- 


 