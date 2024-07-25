from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)


#sitting
for _ in range(1):


    # left back got slight issue, a bit shoter. 
    # elbow
    kit.servo[0].angle = 130
    # inner increase to tilt left 
    kit.servo[1].angle = 100
    # shoulder 
    kit.servo[2].angle = 160

    # left front
    # elbow
    kit.servo[3].angle = 120
    # shoulder
    kit.servo[4].angle = 150
    # inner, decrease to tilt left 
    kit.servo[5].angle = 150 

    # right back
    # inner, increase to tilt left
    kit.servo[6].angle = 115
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 15


    # right front
    # shoulder
    kit.servo[9].angle = 30
    # inner, decrease to tilt left 
    kit.servo[10].angle = 140
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)


