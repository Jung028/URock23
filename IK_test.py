from adafruit_servokit import ServoKit
import time
import math

kit = ServoKit(channels=16)

# Constants
A = 5
E = 15
F = 15.5
I = 9.5
K = 2.5

def calculate_d_and_alpha(Y, Z):
    C = math.sqrt(Y**2 + Z**2)
    D = math.sqrt(C**2 - A**2)
    alpha1 = math.atan2(Z, Y)
    alpha2 = math.atan2(D, A)
    alpha = math.degrees(alpha1 + alpha2)
    return D, alpha

def calculate_b_and_c(X, D):
    G = math.sqrt(D**2 + X**2)
    c = math.degrees(math.acos((G**2 - E**2 - F**2) / (-2 * E * F)))
    b1 = math.atan2(X, D)
    b2 = math.acos((F**2 - E**2 - G**2) / (-2 * E * G))
    b = math.degrees(b1 + b2)
    return b, c

def calculate_j_and_d(X, Z):
    d1 = math.atan2(X, Z)
    e = math.degrees(d1)
    J = math.sqrt(K**2 + I**2 - 2 * K * I * math.cos(math.radians(e)))
    d2 = math.acos((I**2 - J**2 - K**2) / (-2 * J * K))
    d = math.degrees(d1 + d2)
    return J, d

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
        (9, 5), (10, 120), (11, 110)
    ]
    for servo, angle in positions:
        move_servo_smoothly(servo, kit.servo[servo].angle, angle)
    time.sleep(1)

starting_pos()

def perform_step(Y, Z, X):
    D, alpha = calculate_d_and_alpha(Y, Z)
    b, c = calculate_b_and_c(X, D)
    J, d = calculate_j_and_d(X, Z)
    
    angles = [
        (0, alpha), # Example angle for servo 0 based on alpha
        (1, b),     # Example angle for servo 1 based on b
        (2, c),     # Example angle for servo 2 based on c
        (3, d),     # Example angle for servo 3 based on d
        # Add more servo assignments based on the calculations
    ]
    
    for servo, end_angle in angles:
        current_angle = kit.servo[servo].angle
        move_servo_smoothly(servo, current_angle, end_angle)
    time.sleep(1)

# Loop through the steps
Y_values = [10, 20, 15]  # Example Y values for walking steps
Z_values = [10, 15, 20]  # Example Z values for walking steps
X_values = [10, 5, 20]   # Example X values for walking steps

for _ in range(5):
    for Y, Z, X in zip(Y_values, Z_values, X_values):
        perform_step(Y, Z, X)
