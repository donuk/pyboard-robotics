from pyb import Pin, Timer


class Servo:
    """ Class representing a standard servo
    """
    def __init__(self, pin_name, timer_no, channel):
        """ Create a pwm channel on the specified
        pin using the specified timer """
        self.pin = Pin(pin_name)
        self.timer = Timer(timer_no, freq=50)
        self.channel = self.timer.channel(channel, Timer.PWM, pin=self.pin)

    def forward(self):
        """ Intended for use with continuous
        modified servos. Move the motor forward """
        self.degrees(180)

    def backward(self):
        """ Intended for use with continuous
        modified servos. Move the motor backward """
        self.degrees(0)

    def stop(self):
        """ Stop the PWM signal, causes the 
        servo to stop where it is """
        self.channel.pulse_width_percent(0)

    def degrees(self, degrees):
        """ Move the servo to the specified
        position in degrees (between 0 and 180)
        This is not 100% accurate. """
        # Map the angle into the range 2.5-12.5
        fractional_angle = degrees/180.0
        duty_percent = 2.5+fraction*10
        # Set the pulse width
        self.channel.pulse_width_percent(duty_percent)


# Create servos based on the servo shield 
# pins and the pyboard's timer mappings
servo1 = Servo('Y1',8,1)
servo2 = Servo('Y2',8,2)
servo3 = Servo('Y3',4,3)
servo4 = Servo('Y4',4,4)
