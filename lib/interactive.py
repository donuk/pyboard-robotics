# main.py -- put your code here!
from lib.servo import servo1, servo2, stop_servos_before_finishing
from lib.accelerometer import accelerometer


def forward():
    servo1.forward()
    servo2.forward()


def stop():
    servo1.stop()
    servo2.stop()


def left():
    servo1.forward()
    servo2.backward()


def right():
    servo1.backward()
    servo2.forward()


def backward():
    servo1.backward()
    servo2.backward()


go = forward
back = backward
reverse = backward
rev = backward
