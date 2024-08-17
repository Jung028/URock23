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

# Define the target angles for standing and sitting
angles_standing = [
    100, 120, 160,  # left back
    120, 150, 120,  # left front
    120, 110, 30,   # right back
    30, 120, 110    # right front
]

angles_sitting = [
    180, 120, 180,  # left back
    180, 180, 120,  # left front
    120, 0, 0,      # right back
    0, 120, 0       # right front
]

# Main loop
while True:
    # Smooth transition to standing position
    set_servo_angles(angles_standing)
    time.sleep(2)
    
    # Smooth transition to sitting position
    set_servo_angles(angles_sitting)
    time.sleep(2)
