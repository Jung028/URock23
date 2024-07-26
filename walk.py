from adafruit_servokit import ServoKit
import time

# Initialize ServoKit with the number of servo channels (16 in this case)
kit = ServoKit(channels=16)

# Initial positions for all servos
initial_positions = {
    0: 150,  # Left back elbow
    1: 120,  # Left back inner
    2: 170,  # Left back shoulder
    3: 120,  # Left front elbow
    4: 170,  # Left front shoulder
    5: 130,  # Left front inner
    6: 130,  # Right back inner
    7: 60,   # Right back elbow
    8: 5,    # Right back shoulder
    9: 5,    # Right front shoulder
    10: 120, # Right front inner
    12: 110  # Right front elbow
}

# Set initial positions
for servo, angle in initial_positions.items():
    kit.servo[servo].angle = angle

time.sleep(2)

# Define movements for each servo
def move_servo(servo_angles):
    for servo, angle in servo_angles.items():
        kit.servo[servo].angle = angle
    time.sleep(0.1)

# Interpolate between two angles
def interpolate(start_angle, end_angle, steps):
    return [start_angle + (end_angle - start_angle) * i / (steps - 1) for i in range(steps)]

# Define sequences for each leg with smooth transitions
def smooth_transition(sequence, steps=30):
    for i in range(len(sequence) - 1):
        start_angles = sequence[i]
        end_angles = sequence[i + 1]
        
        angles_interpolation = {}
        for servo in start_angles.keys():
            start_angle = start_angles[servo]
            end_angle = end_angles[servo]
            angles_interpolation[servo] = interpolate(start_angle, end_angle, steps)
        
        # Perform smooth transition
        for step in range(steps):
            for servo, angles in angles_interpolation.items():
                kit.servo[servo].angle = angles[step]
            time.sleep(0.1)

# Define sequences
left_back_sequence = [
    {0: 180, 1: 120, 2: 170},
    {0: 150, 1: 120, 2: 140},
    {0: 130, 1: 120, 2: 180}
]

right_front_sequence = [
    {9: 5, 10: 120, 12: 80},
    {9: 25, 10: 120, 12: 110},
    {9: 0, 10: 120, 12: 120}
]

left_front_sequence = [
    {3: 140, 4: 170, 5: 130},
    {3: 100, 4: 150, 5: 130},
    {3: 130, 4: 180, 5: 130}
]

right_back_sequence = [
    {6: 130, 7: 30, 8: 5},
    {6: 130, 7: 70, 8: 25},
    {6: 130, 7: 50, 8: 0}
]

# Perform smooth transitions for each leg
for _ in range(4):
    smooth_transition(left_back_sequence)
    smooth_transition(right_front_sequence)
    smooth_transition(left_front_sequence)
    smooth_transition(right_back_sequence)
