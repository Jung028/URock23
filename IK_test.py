from adafruit_servokit import ServoKit
import time
import math

# Initialize the servo kit
kit = ServoKit(channels=16)

# Standing position angles
def set_standing_position():
    # Left back
    kit.servo[0].angle = 100  # elbow
    kit.servo[1].angle = 120  # inner
    kit.servo[2].angle = 160  # shoulder

    # Left front
    kit.servo[3].angle = 120  # elbow
    kit.servo[4].angle = 150  # shoulder
    kit.servo[5].angle = 120  # inner

    # Right back
    kit.servo[6].angle = 120  # inner
    kit.servo[7].angle = 110  # elbow
    kit.servo[8].angle = 30   # shoulder

    # Right front
    kit.servo[9].angle = 30   # shoulder
    kit.servo[10].angle = 120 # inner
    kit.servo[12].angle = 110 # elbow

    time.sleep(1)  # Hold the standing position for 1 second

# Function definitions for inverse kinematics calculations
def compute_a(Z, Y, D, A):
    return math.atan2(Z, Y) + math.atan2(D, A)

def compute_D(Y, Z):
    return math.sqrt((math.sqrt(Y**2 + Z**2))**2 - 25)

def compute_c(G, E, F):
    return math.acos((G**2 - E**2 - F**2) / (-2 * E * F))

def compute_b(X, D, F, E, G):
    term1 = math.atan2(X, D)
    term2 = math.acos((F**2 - E**2 - G**2) / (-2 * E * G))
    return term1 + term2

def compute_d(X, Z, J):
    term1 = math.atan2(X, Z)
    term2 = math.acos((90.25 - J**2 - 6.25) / (-5 * J))
    return term1 + term2

def compute_J(e):
    return math.sqrt(49 * math.cos(e))

# Function to send motor commands
def set_servo_angles(leg_id, a, b, c):
    # Assuming leg_id 0 is left back, 1 is left front, 2 is right back, 3 is right front
    if leg_id == 0:
        kit.servo[0].angle = math.degrees(a)  # elbow
        kit.servo[1].angle = math.degrees(b)  # inner
        kit.servo[2].angle = math.degrees(c)  # shoulder
    elif leg_id == 1:
        kit.servo[3].angle = math.degrees(a)  # elbow
        kit.servo[4].angle = math.degrees(b)  # shoulder
        kit.servo[5].angle = math.degrees(c)  # inner
    elif leg_id == 2:
        kit.servo[6].angle = math.degrees(a)  # inner
        kit.servo[7].angle = math.degrees(b)  # elbow
        kit.servo[8].angle = math.degrees(c)  # shoulder
    elif leg_id == 3:
        kit.servo[9].angle = math.degrees(a)  # shoulder
        kit.servo[10].angle = math.degrees(b) # inner
        kit.servo[12].angle = math.degrees(c) # elbow

# Example inverse kinematics for a trot gait
def trot_gait(step_height, step_length, duration):
    set_standing_position()  # Set the robot to the standing position
    time.sleep(1)  # Wait for a moment before starting the gait
    
    for t in range(duration):
        # Calculate foot positions for each leg based on time t
        if t % 2 == 0:
            # Left front and right back up, right front and left back down
            lf_pos = (step_length, 0, step_height * math.sin(math.pi * t / duration))
            rb_pos = (step_length, 0, step_height * math.sin(math.pi * t / duration))
            rf_pos = (0, 0, 0)
            lb_pos = (0, 0, 0)
        else:
            # Right front and left back up, left front and right back down
            rf_pos = (step_length, 0, step_height * math.sin(math.pi * t / duration))
            lb_pos = (step_length, 0, step_height * math.sin(math.pi * t / duration))
            lf_pos = (0, 0, 0)
            rb_pos = (0, 0, 0)

        # Compute angles for each leg using inverse kinematics
        lf_angles = (compute_a(*lf_pos), compute_b(*lf_pos), compute_c(*lf_pos))
        rf_angles = (compute_a(*rf_pos), compute_b(*rf_pos), compute_c(*rf_pos))
        lb_angles = (compute_a(*lb_pos), compute_b(*lb_pos), compute_c(*lb_pos))
        rb_angles = (compute_a(*rb_pos), compute_b(*rb_pos), compute_c(*rb_pos))

        # Print the computed angles and foot positions for debugging
        print(f"Iteration {t}:")
        print(f"Foot Positions - Left Front: {lf_pos}, Right Front: {rf_pos}, Left Back: {lb_pos}, Right Back: {rb_pos}")
        print(f"Left Front Leg Angles: {lf_angles}")
        print(f"Right Front Leg Angles: {rf_angles}")
        print(f"Left Back Leg Angles: {lb_angles}")
        print(f"Right Back Leg Angles: {rb_angles}")

        # Set the servo angles
        # set_servo_angles(1, *lf_angles)
        # set_servo_angles(3, *rf_angles)
        # set_servo_angles(0, *lb_angles)
        # set_servo_angles(2, *rb_angles)

        time.sleep(0.1)  # Adjust the sleep time to control the speed of the gait

# Example usage
trot_gait(step_height=5, step_length=10, duration=10)
