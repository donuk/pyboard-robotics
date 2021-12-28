# main.py -- put your code here!
from time import sleep
from lib.servo import servo1, servo2, stop_servos_before_finishing


turn_left = True

# This will stop the servos if anything goes wrong
with stop_servos_before_finishing():
    # Loop forever
    while True:

        # To turn we have to run the servos
        # at different speeds so choose a
        # fast servo and a slow servo based
        # on the setting in turn_left
        if turn_left:
            fast_servo = servo1
            slow_servo = servo2
        else:
            fast_servo = servo2
            slow_servo = servo1

        # Run the fast servo at full speed
        fast_servo.forward()

        # Repeat 20 times switch the slow servo
        # on and off. Waiting 0.1 seconds each
        # time
        for counter in range(0, 20):
            slow_servo.forward()
            sleep(0.1)
            slow_servo.stop()
            sleep(0.1)

        # Change the setting in turn_left so
        # that next time we change the other
        # direction
        turn_left = not turn_left
