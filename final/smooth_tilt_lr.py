from adafruit_servokit import ServoKit
import time
import numpy as np

# Initialize ServoKit
kit = ServoKit(channels=16)

# Function to interpolate between two angles
def interpolate(start_angle, end_angle, steps, delay):
    for step in range(steps):
        angle = start_angle + (end_angle - start_angle) * (step / steps)
        yield angle
        time.sleep(delay)

# Function to set servo angles with interpolation
def set_servo_angles(angles, steps=10, delay=0.05):
    current_angles = [servo.angle for servo in kit.servo]
    for i, (target_angle, servo) in enumerate(zip(angles, kit.servo)):
        for angle in interpolate(current_angles[i], target_angle, steps, delay):
            servo.angle = angle

# Define the target angles for standing, tilting left, and tilting right
angles_stand = [
    150, 120, 170,  # left back
    120, 170, 130,  # left front
    130, 60, 5,     # right back
    5, 120, 110     # right front
]

angles_tilt_left = [
    130, 140, 160,  # left back
    120, 150, 110,  # left front
    155, 60, 15,    # right back
    30, 100, 110    # right front
]

angles_tilt_right = [
    130, 100, 160,  # left back
    120, 150, 150,  # left front
    115, 60, 15,    # right back
    30, 140, 110    # right front
]

# Move to standing position
set_servo_angles(angles_stand)
time.sleep(1)  # Hold standing position for 1 second

# Main loop
for _ in range(5):
    set_servo_angles(angles_tilt_left)
    time.sleep(1)
    
    set_servo_angles(angles_tilt_right)
    time.sleep(1)
