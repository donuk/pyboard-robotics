from pyb import Pin, Timer


class Servo:
    def __init__(self, pin_name, timer_no, channel):
        self.pin = Pin(pin_name)
        self.timer = Timer(timer_no, freq=50)
        self.channel = self.timer.channel(channel, Timer.PWM, pin=self.pin)

    def forward(self):
        self.degrees(180)
    def backward(self):
        self.degrees(0)

    def stop(self):
        self.channel.pulse_width_percent(0)

    def degrees(self, degrees):
        fraction = degrees/180.0
        self.channel.pulse_width_percent(2.5+fraction*10)


servo1 = Servo('Y1',8,1)
servo2 = Servo('Y2',8,2)
servo3 = Servo('Y3',4,3)
servo4 = Servo('Y4',4,4)
