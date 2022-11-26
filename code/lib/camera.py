import board
import digitalio

class Camera():

    button = None
    power  = None

    def __init__(self, button, power):
        self.button = digitalio.DigitalInOut(button)
        self.button.switch_to_input(pull = digitalio.Pull.UP)

        self.power = digitalio.DigitalInOut(power)
        self.power.direction = digitalio.Direction.OUTPUT
        self.deactivate()

    def activate(self):
        self.power_status(True)

    def deactivate(self):
        self.power_status(False)

    def button_status(self):
        return not self.button.value

    def power_status(self, status):
        self.power.value = status
