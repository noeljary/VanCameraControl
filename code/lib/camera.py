import board
import digitalio

class Camera():

    button = None
    power  = None
    status = False

    SEL_A = digitalio.DigitalInOut(board.GP17)
    SEL_A.direction = digitalio.Direction.OUTPUT
    SEL_B = digitalio.DigitalInOut(board.GP16)
    SEL_B.direction = digitalio.Direction.OUTPUT

    def __init__(self, button, power, sel_a, sel_b):
        self.sel_a = sel_a
        self.sel_b = sel_b

        self.button = digitalio.DigitalInOut(button)
        self.button.switch_to_input(pull = digitalio.Pull.UP)

        self.power = digitalio.DigitalInOut(power)
        self.power.direction = digitalio.Direction.OUTPUT
        self.deactivate()

    def activate(self):
        Camera.SEL_A.value = self.sel_a
        Camera.SEL_B.value = self.sel_b
        self.power_status(True)
        self.status = True

    def deactivate(self):
        self.power_status(False)
        self.status = False

    def button_status(self):
        return not self.button.value

    def power_status(self, status):
        self.power.value = status

    def getStatus(self):
        return self.status
