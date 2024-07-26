from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

def move_servo_smoothly(servo, start_angle, end_angle, steps=10, delay=0.05):
    # Ensure the angles are within the valid range
    start_angle = max(0, min(180, start_angle))
    end_angle = max(0, min(180, end_angle))
    # Calculate the step size
    step_size = (end_angle - start_angle) / steps
    # Gradually move the servo to the target angle
    for i in range(steps):
        angle = start_angle + step_size * i
        angle = max(0, min(180, angle))
        kit.servo[servo].angle = angle
        time.sleep(delay)
    kit.servo[servo].angle = end_angle

# Function to set the servos to the specified positions smoothly
def set_positions_smoothly(positions, steps=10, delay=0.05):
    for servo, end_angle in positions:
        current_angle = kit.servo[servo].angle
        move_servo_smoothly(servo, current_angle, end_angle, steps, delay)

# Sitting positions
sitting_positions_1 = [
    (0, 130), (1, 120), (2, 160),
    (3, 120), (4, 150), (5, 130),
    (6, 135), (7, 60), (8, 15),
    (9, 30), (10, 120), (12, 110)
]

sitting_positions_2 = [
    (0, 130), (1, 120), (2, 180),
    (3, 120), (4, 180), (5, 130),
    (6, 135), (7, 60), (8, 10),
    (9, 10), (10, 120), (12, 110)
]

# Move to sitting positions
for _ in range(2):
    set_positions_smoothly(sitting_positions_1, steps=20, delay=0.02)
    time.sleep(1)
    set_positions_smoothly(sitting_positions_2, steps=20, delay=0.02)
    time.sleep(1)
