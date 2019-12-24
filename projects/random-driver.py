# main.py -- put your code here!
from time import sleep
from lib.servo import servo1, servo2, servo3, servo4
from random import choice, randint


all_servos = [ servo1, servo2, servo3, servo4]
all_actions = [ "turn" , "stop" ] 

# The try/except block allows us to stop 
# the servos if anything goes wrong
try:
    # Loop forever
    while True:
        # Loop through all servos
        for current_servo in all_servos:

            # Choose a random action
            action = choice(all_actions)

            if action=="turn":
                # Choose a random angle between 0 and 180
                angle = randint(0,180)

                # Turn to the chosen angle
                # Note: for modified servos
                # certain angles will cause
                # the motor to move forward
                # and others will move backward

                servo.degrees(angle)

            if action == "stop":
                servo.stop()

        # Wait 1/2 a second before repeating
        sleep(0.5)
except:
    # Something's gone wrong stop all the
    # servos before we exit
    servo1.stop()
    servo2.stop()
    servo3.stop()
    servo4.stop()
    raise
