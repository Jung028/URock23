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

# Define the target angles for sway forward and backward
angles_sway_forward = [
    130, 120, 160,  # left back
    120, 150, 130,  # left front
    135, 60, 15,    # right back
    30, 120, 110    # right front
]

angles_sway_backward = [
    130, 120, 180,  # left back
    120, 180, 130,  # left front
    135, 60, 10,    # right back
    10, 120, 110    # right front
]

# Main loop
for _ in range(2):
    set_servo_angles(angles_sway_forward)
    time.sleep(1)

    set_servo_angles(angles_sway_backward)
    time.sleep(1)
