from adafruit_servokit import ServoKit
import time

#Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

#standing
while True :

    # 3 - inner
    # 2 - shoulder
    # 1 - elbow

    time.sleep(2)
    
    #-------------------------
    #STANDING

    # left back got slight issue, a bit shoter. 
    # elbow
    kit.servo[0].angle = 100
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 160





    # left front
    # elbow
    kit.servo[3].angle = 120
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 120




    # right back
    # inner
    kit.servo[6].angle = 120
    # elbow
    kit.servo[7].angle = 110
    # shoulder
    kit.servo[8].angle = 30



    # right front
    # shoulder
    kit.servo[9].angle = 30
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110


    time.sleep(2)


    #-------------------------
    # SITTING



    # left back
    # elbow`
    kit.servo[0].angle = 180
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 180





    # left front
    # elbow
    kit.servo[3].angle = 180
    # shoulder
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 120




    # right back
    # inner
    kit.servo[6].angle = 120
    # elbow
    kit.servo[7].angle = 0
    # shoulder
    kit.servo[8].angle = 0



    # right front
    # shoulder
    kit.servo[9].angle = 0
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 0






