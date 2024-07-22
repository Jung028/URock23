from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

#sitting
while True :

    # 3 - inner
    # 2 - shoulder
    # 1 - elbow

    # STAND
    # elbow
    kit.servo[0].angle = 100
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 160
   
    time.sleep(1)

    # left back
    # elbow
    kit.servo[0].angle = 180
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 160
   
    time.sleep(1)

    # elbow
    kit.servo[0].angle = 100
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 90
   
    time.sleep(1)


    # time.sleep(1)

    # kit.servo[0].angle = 160


    # time.sleep(1)

    # kit.servo[0].angle = 140

    # time.sleep(1)



    # elbow
    # inner
    # shoulder 


