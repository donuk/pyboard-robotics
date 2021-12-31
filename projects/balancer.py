# main.py -- put your code here!
from lib.servo import servo1, stop_servos_before_finishing
from lib.accelerometer import accelerometer


turn_left = True

# This will stop the servos if anything goes wrong
with stop_servos_before_finishing():
    # Loop forever
    while True:
        x = accelerometer.x()
        if x < -5:
            servo1.forward()
        elif x > 5:
            servo1.backward()
        else:
            servo1.stop()
