from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

int left_max_angle_LB = 140 
int left_max_angle_LF = 110 
int left_max_angle_RB = 155
int left_max_angle_RF = 100 

int right_max_angle_LB = 100 
int right_max_angle_LF = 150 
int right_max_angle_RB = 115
int right_max_angle_RF = 140 

int left_LB = 140

#sitting
for _ in range(2):

    # add a loop to iterate through the 4 tilt left angles to the 4 tilt right angles
    for _ in range(left_max_angle_LB - right_max_angle_LB) :
        left_LB += 1 

    
    # left back got slight issue, a bit shoter. 
    # elbow
    kit.servo[0].angle = 130
    # inner increase to tilt left 
    kit.servo[1].angle = 140
    # shoulder 
    kit.servo[2].angle = 160

    # left front
    # elbow
    kit.servo[3].angle = 120
    # shoulder
    kit.servo[4].angle = 150
    # inner, decrease to tilt left 
    kit.servo[5].angle = 110 

    # right back
    # inner, increase to tilt left
    kit.servo[6].angle = 155
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 15


    # right front
    # shoulder
    kit.servo[9].angle = 30
    # inner, decrease to tilt left 
    kit.servo[10].angle = 100
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)


    # Tilt RIGHT 

    # left back got slight issue, a bit shoter. 
    # elbow
    kit.servo[0].angle = 130
    # inner decrease to tilt right 
    kit.servo[1].angle = 100
    # shoulder 
    kit.servo[2].angle = 160

    # left front
    # elbow
    kit.servo[3].angle = 120
    # shoulder
    kit.servo[4].angle = 150
    # inner, increase to tilt right 
    kit.servo[5].angle = 150 

    # right back
    # inner, decrease to tilt right
    kit.servo[6].angle = 115
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 15


    # right front
    # shoulder
    kit.servo[9].angle = 30
    # inner, increase to tilt right 
    kit.servo[10].angle = 140
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)

