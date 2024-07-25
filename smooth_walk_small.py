from adafruit_servokit import ServoKit
import time

# Set channels to the number of servo channels on your driver. Most likely 16 or 8.
kit = ServoKit(channels=16)

def move_servo_smoothly(servo, start_angle, end_angle, steps=10, delay=0.05):
    step_size = (end_angle - start_angle) / steps
    for i in range(steps):
        kit.servo[servo].angle = start_angle + step_size * i
        time.sleep(delay)
    kit.servo[servo].angle = end_angle

def starting_pos(): 
    positions = [
        (0, 150), (1, 120), (2, 170),
        (3, 120), (4, 170), (5, 130),
        (6, 130), (7, 60), (8, 5),
        (9, 5), (10, 120), (12, 110)
    ]
    for servo, angle in positions:
        move_servo_smoothly(servo, kit.servo[servo].angle, angle)
    time.sleep(1)

starting_pos()

def perform_step(angles):
    for servo, end_angle in angles:
        current_angle = kit.servo[servo].angle
        move_servo_smoothly(servo, current_angle, end_angle)
    time.sleep(1)

# Define the sequence of steps with gradual changes
steps = [
    # Step 1
    [
        (0, 150), (1, 120), (2, 170),
        (3, 120), (4, 170), (5, 130),
        (6, 130), (7, 60), (8, 5),
        (9, 5), (10, 120), (12, 110)
    ],
    # Step 2
    [
        (0, 130), (1, 120), (2, 170),
        (3, 120), (4, 175), (5, 130),
        (6, 130), (7, 35), (8, 0),
        (9, 5), (10, 120), (12, 90)
    ],
    # Step 3
    [
        (0, 130), (1, 120), (2, 160),
        (3, 120), (4, 180), (5, 130),
        (6, 130), (7, 60), (8, 0),
        (9, 15), (10, 120), (12, 120)
    ],
    # Step 4
    [
        (0, 130), (1, 120), (2, 175),
        (3, 100), (4, 160), (5, 130),
        (6, 130), (7, 60), (8, 20),
        (9, 20), (10, 120), (12, 160)
    ],
    # Step 5
    [
        (0, 160), (1, 118), (2, 160),
        (3, 100), (4, 170), (5, 130),
        (6, 130), (7, 60), (8, 10),
        (9, 30), (10, 120), (12, 110)
    ],
    # Step 6
    [
        (0, 150), (1, 120), (2, 150),
        (3, 100), (4, 180), (5, 130),
        (6, 130), (7, 60), (8, 0),
        (9, 50), (10, 120), (12, 100)
    ],
    # Step 7
    [
        (0, 100), (1, 120), (2, 180),
        (3, 100), (4, 180), (5, 130),
        (6, 130), (7, 60), (8, 0),
        (9, 10), (10, 120), (12, 110)
    ]
]

# Loop through the steps
for _ in range(5):
    for step in steps:
        perform_step(step)
