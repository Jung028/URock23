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
    # right back
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 15

    time.sleep(1)

    # ----------------------------- 

    

    # ----------------------------- POINT 2
    # right back
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 10
    # shoulder
    kit.servo[8].angle = 15

    time.sleep(1)

    # ----------------------------- 



    # ----------------------------- POINT 3
    # right back
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 100
    # shoulder
    kit.servo[8].angle = 50

    time.sleep(1)

    # ----------------------------- 





    # ----------------------------- POINT 4 (Push Back)
    # right back
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 0

    time.sleep(1)

    # ----------------------------- 


    

    # ----------------------------- POINT 2
    # right back
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 10
    # shoulder
    kit.servo[8].angle = 15

    time.sleep(1)

    # ----------------------------- 



    # ----------------------------- POINT 3
    # right back
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 100
    # shoulder
    kit.servo[8].angle = 50

    time.sleep(1)

    # ----------------------------- 



    # ----------------------------- POINT 4 (Push Back)
    # right back
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 0

    time.sleep(1)

    # ----------------------------- 