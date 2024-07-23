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

    
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 130
   
    time.sleep(1)
    # ----------------------------- 

    # STAND


    # LIFT UP ELBOW
    # left back
    # ----------------------------- POINT 2 
    # elbow
    kit.servo[0].angle = 150
    # inner
    kit.servo[1].angle = 118
    # shoulder 
    kit.servo[2].angle = 160

    kit.servo[3].angle = 140
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 133
   
    time.sleep(0.3)
    # -----------------------------


    # ----------------------------- POINT 3 
    # elbow
    kit.servo[0].angle = 80
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 130

    kit.servo[3].angle = 70
    # shoulder
    kit.servo[4].angle = 120
    # inner 
    kit.servo[5].angle = 133
   
    time.sleep(1)
    # -----------------------------


    # ----------------------------- POINT 4 (Push Back)
    # elbow
    kit.servo[0].angle = 100
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 180

    # elbow
    kit.servo[3].angle = 100
    # shoulder
    kit.servo[4].angle = 180
    # inner 
    kit.servo[5].angle = 130
   
    time.sleep(1)
    # -----------------------------



    # LIFT UP ELBOW
    # left back
    # ----------------------------- POINT 2 
   # elbow
    kit.servo[0].angle = 150
    # inner
    kit.servo[1].angle = 118
    # shoulder 
    kit.servo[2].angle = 160

    kit.servo[3].angle = 140
    # shoulder
    kit.servo[4].angle = 150
    # inner 
    kit.servo[5].angle = 133
   
    time.sleep(0.3)
    # -----------------------------

    # ----------------------------- POINT 3 
     # elbow
    kit.servo[0].angle = 80
    # inner
    kit.servo[1].angle = 120
    # shoulder 
    kit.servo[2].angle = 130

    kit.servo[3].angle = 70
    # shoulder
    kit.servo[4].angle = 120
    # inner 
    kit.servo[5].angle = 133
   
    time.sleep(1)
    # -----------------------------

