from pyb import Pin, ExtInt
from micropython import schedule


class Button:
    _pin = None
    _interrupt = None

    def __init__(self, pin_name):
        self.pin_name = pin_name

    def __del__(self):
        for interrupt in self._interrupts:
            interrupt.disable()

    @property
    def pin(self):
        if not self._pin:
            self.pin = Pin(
                self.pin_name,
                mode=Pin.IN,
                pull=Pin.PULL_DOWN
            )

        return self._pin

    def on_press(self, callback, args=[], kwargs={}):
        self._interrupts.append(
            ExtInt(
                self.pin_name,
                ExtInt.IRQ_RISING,
                Pin.PULL_DOWN,
                lambda: schedule(
                    lambda: callback(*args, **kwargs)
                )
            )
        )

    def get_state(self):
        return self.pin.value() != 0
