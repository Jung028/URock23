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
    # Starting position
    positions = [
        (0, 130), (1, 120), (2, 160),
        (3, 120), (4, 150), (5, 130),
        (6, 135), (7, 60), (8, 15),
        (9, 30), (10, 120), (12, 110)
    ]
    for servo, angle in positions:
        kit.servo[servo].angle = angle
    time.sleep(1)

starting_pos()

# Walking sequence
sequence = [
    # Point 2
    [(0, 100), (2, 180), (7, 35), (9, 10)],
    # Point 3
    [(0, 110), (2, 165), (4, 130), (7, 30), (12, 130)],
    # Point 4
    [(0, 90), (2, 175), (3, 100), (4, 160), (12, 160)],
    # Point 5
    [(0, 160), (2, 160)],
    # Point 6
    [(0, 150), (2, 150), (9, 50), (12, 100)],
    # Point 7
    [(0, 100), (2, 180), (9, 10), (12, 110)]
]

# Execute the sequence smoothly
for _ in range(5):
    for step in sequence:
        for servo, end_angle in step:
            current_angle = kit.servo[servo].angle
            move_servo_smoothly(servo, current_angle, end_angle)
        time.sleep(0.5)
