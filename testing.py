from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

# STANDING POSITION 
# left back got slight issue, a bit shoter. 
# elbow
kit.servo[0].angle = 130
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
kit.servo[5].angle = 130




# right back
# inner
kit.servo[6].angle = 135
# elbow
kit.servo[7].angle = 60
# shoulder
kit.servo[8].angle = 15



# right front
# shoulder
kit.servo[9].angle = 30
# inner 
kit.servo[10].angle = 120
# elbow
kit.servo[12].angle = 110

time.sleep(1)

# the position of the leg that touch the ground is not the same, so the tilt of the robot causes 
# the robot legs to not be able to lift above the ground. 

#sitting
for _ in range(4):

  # ----------------------------- POINT 2 (Right front and left back lift up )
    #LEFT BACK
    # elbow
    kit.servo[0].angle = 100
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[13].angle = 170


    #LEFT FRONT
    # elbow
    kit.servo[3].angle = 120
    # shoulder
    kit.servo[4].angle = 160
    # inner 
    kit.servo[5].angle = 133

    #RIGHT BACK
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 35
    # shoulder
    kit.servo[8].angle = 15

    # right front
    # shoulder
    kit.servo[9].angle = 20
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)


    # ----------------------------- POINT 3 (Right front and left back lift up )

    #LEFT BACK 
    # elbow
    kit.servo[0].angle = 100
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[13].angle = 175

    #LEFT FRONT 
    # elbow
    kit.servo[3].angle = 80
    # shoulder
    kit.servo[4].angle = 140
    # inner 
    kit.servo[5].angle = 133


    #RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 20



    #RIGHT FRONT 
    # shoulder
    kit.servo[9].angle = 15
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 130

    time.sleep(1)

    # ----------------------------- 

 



    # ----------------------------- POINT 4 (Left right and right back push back ) 

    #LEFT BACK 
    kit.servo[0].angle = 100
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[13].angle = 180

    #LEFT FRONT 
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 160
    # inner 
    kit.servo[5].angle = 130

    #RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 20
    # elbow

     #RIGHT FRONT 
    # shoulder
    kit.servo[9].angle = 10
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 130

    time.sleep(1)

    # ----------------------------- 






    # ----------------------------- POINT 5 (Right front and left back lift up )
    

    # Left Back 
    # elbow
    kit.servo[0].angle = 150
    # inner
    kit.servo[1].angle = 118
    # shoulder 
    kit.servo[13].angle = 170
       
    #LEFT FRONT 
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 170
    # inner 
    kit.servo[5].angle = 130

    #RIGHT BACK 
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 10
    # elbow

    # Right front
    # shoulder
    kit.servo[9].angle = 30
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)

    # ----------------------------- 






   # ----------------------------- POINT 6 (Right front and left back bring forward)

    #left back and right front bring forward

  
    # LEFT BACK 
    # elbow 
    kit.servo[0].angle = 150 # THIS 
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[13].angle = 160

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



    # RIGHT FRONT
    # shoulder
    kit.servo[9].angle = 32
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 100 #THIS

    time.sleep(1)


    # ----------------------------- 




    # ----------------------------- POINT 7 (Right front and left back push back)
 
    #LEFT BACK
    # elbow
    kit.servo[0].angle = 100
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[13].angle = 170


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

    # right front
    # shoulder
    kit.servo[9].angle = 20
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110


    time.sleep(1)
    # ----------------------------- 

