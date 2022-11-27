import board
import digitalio
import time

class Latch():

    status = True

    def __init__(self, button, led):
        self.button = digitalio.DigitalInOut(button)
        self.button.switch_to_input(pull = digitalio.Pull.UP)

        self.led = digitalio.DigitalInOut(led)
        self.led.direction = digitalio.Direction.OUTPUT

        self.activate()

    def activate(self):
        self.led_status(True)
        self.status = True

    def deactivate(self):
        self.led_status(False)
        self.status = False

    def button_status(self):
        return not self.button.value

    def led_status(self, status):
        self.led.value = status

    def scan(self):
        if self.button_status():
            while self.button_status():
                time.sleep(0.01)
            self.deactivate() if self.getStatus() else self.activate()
            time.sleep(0.1)

    def getStatus(self):
        return self.status

