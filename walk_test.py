from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)


#sitting
for _ in range(1):

# AFter properly developing the code for the walking motion where all the angles are correct, then you can 
# Create a loop. to increase the values all the way to the angles for the next position. 

    # left back got slight issue, a bit shoter. 
    # elbow
    kit.servo[0].angle = 150
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 170


    # left front
    # elbow
    kit.servo[3].angle = 120
    # shoulder
    kit.servo[4].angle = 170
    # inner 
    kit.servo[5].angle = 130


    # right back
    # inner
    kit.servo[6].angle = 130
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 5



    # right front
    # shoulder
    kit.servo[9].angle = 5
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)


    #------------------------------------------
    # left back got slight issue, a bit shoter. 
    # elbow INCREASE 20 
    kit.servo[0].angle = 150
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 170

    # left front
    # elbow
    kit.servo[3].angle = 120
    # shoulder INCREASE 5 
    kit.servo[4].angle = 175
    # inner 
    kit.servo[5].angle = 130

    # right back
    # inner
    kit.servo[6].angle = 130
    # elbow
    kit.servo[7].angle = 60
    # shoulder DECREASE 5  
    kit.servo[8].angle = 0

    # right front
    # shoulder
    kit.servo[9].angle = 5
    # inner 
    kit.servo[10].angle = 120
    # elbow DECREASE 20 
    kit.servo[12].angle = 90

    time.sleep(1)
    #------------------------------------------






    #------------------------------------------
    # left back got slight issue, a bit shoter. 
    # elbow DECREASE 30 
    kit.servo[0].angle = 130
    # inner
    kit.servo[1].angle = 120
    # shoulder DECREASE 10 
    kit.servo[2].angle = 160

    # left front
    # elbow
    kit.servo[3].angle = 120
    # shoulder INCREASE 5
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130

    # right back
    # inner
    kit.servo[6].angle = 130
    # elbow
    kit.servo[7].angle = 60
    # shoulder DECREASE 5 but still 0 
    kit.servo[8].angle = 0

    # right front
    # shoulder INCREASE 10
    kit.servo[9].angle = 15
    # inner 
    kit.servo[10].angle = 120
    # elbow INCREASE 30
    kit.servo[12].angle = 120 

    time.sleep(1)
    #------------------------------------------




    #------------------------------------------
    # left back got slight issue, a bit shoter. 
    # elbow DECREASE 30 
    kit.servo[0].angle = 130
    # inner
    kit.servo[1].angle = 120
    # shoulder DECREASE 10 
    kit.servo[2].angle = 170

    # left front
    # elbow
    kit.servo[3].angle = 120
    # shoulder INCREASE 5
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130

    # right back
    # inner
    kit.servo[6].angle = 130
    # elbow
    kit.servo[7].angle = 60
    # shoulder DECREASE 5 but still 0 
    kit.servo[8].angle = 0

    # right front
    # shoulder INCREASE 10
    kit.servo[9].angle = 5
    # inner 
    kit.servo[10].angle = 120
    # elbow INCREASE 30
    kit.servo[12].angle = 120 

    time.sleep(1)
    #------------------------------------------
