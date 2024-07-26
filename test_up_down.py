



from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)


#sitting
for _ in range(1):


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



# First, All 4 legs move back. 






    # left back got slight issue, a bit shoter. 
    # elbow
    kit.servo[0].angle = 130
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 180





    # left front
    # elbow
    kit.servo[3].angle = 120
    # shoulder
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130




    # right back
    # inner
    kit.servo[6].angle = 135
    # elbow
    kit.servo[7].angle = 60
    # shoulder
    kit.servo[8].angle = 10



    # right front
    # shoulder
    kit.servo[9].angle = 10
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    time.sleep(1)


# Try, single leg, lift up, then back to stand position. 



    # ------------------------LEFT BACK----------------------------------
 

    # left back got slight issue, a bit shoter. 
    # elbow
    kit.servo[0].angle = 180
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 170

    time.sleep(0.1)

    # left back got slight issue, a bit shoter. 
    # elbow
    kit.servo[0].angle = 150
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 150

    time.sleep(0.1)

    # left back got slight issue, a bit shoter. 
    # elbow
    kit.servo[0].angle = 130
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 180

    time.sleep(0.1)


    # ------------------------LEFT BACK----------------------------------



    # ------------------------RIGHT FRONT----------------------------------
 

    # right front
    # shoulder
    kit.servo[9].angle = 5
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 70

    time.sleep(0.1)

    # right front
    # shoulder
    kit.servo[9].angle = 25
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 110

    time.sleep(0.1)

    # right front
    # shoulder
    kit.servo[9].angle = 0
    # inner 
    kit.servo[10].angle = 120
    # elbow
    kit.servo[12].angle = 120

    time.sleep(0.1)

    # ------------------------RIGHT FRONT----------------------------------




    # ------------------------LEFT FRONT----------------------------------
  
      # left front
    # elbow
    kit.servo[3].angle = 140
    # shoulder
    kit.servo[4].angle = 170
    # inner 
    kit.servo[5].angle = 130

    time.sleep(0.1)

      # left front
    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 130

    time.sleep(0.1)

     # left front
    # elbow
    kit.servo[3].angle = 110
    # shoulder
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130

    time.sleep(0.1)




    # ------------------------LEFT FRONT----------------------------------




    # ------------------------RIGHT BACK----------------------------------
 

    # right back
    # inner
    kit.servo[6].angle = 130
    # elbow
    kit.servo[7].angle = 30
    # shoulder
    kit.servo[8].angle = 5

    time.sleep(0.1)

    # right back
    # inner
    kit.servo[6].angle = 130
    # elbow
    kit.servo[7].angle = 70
    # shoulder
    kit.servo[8].angle = 25

    time.sleep(0.1)

    # right back
    # inner
    kit.servo[6].angle = 130
    # elbow
    kit.servo[7].angle = 50
    # shoulder
    kit.servo[8].angle = 0

    time.sleep(0.1)

    # ------------------------RIGHT BACK----------------------------------


# Repeat for all 4 
# repeat from start. 