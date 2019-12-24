# main.py -- put your code here!
from time import sleep
from lib.servo import servo1, servo2, servo3, servo4
from random import choice, randint


try:
    while True:
        servos = [ servo1, servo2, servo3, servo4]
        for servo in servos:
            run = choice([
                lambda servo:servo.degrees(randint(0,180)),
                lambda servo:servo.stop(),
            ])
            run(servo)
        sleep(0.5)
except:
    servo1.stop()
    servo2.stop()
    servo3.stop()
    servo4.stop()
    raise
