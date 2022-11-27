import board
import digitalio
import time

from camera import Camera
from latch  import Latch

rev_trigger  = digitalio.DigitalInOut(board.GP26)
rev_trigger.switch_to_input(pull = digitalio.Pull.DOWN)

radio_signal = digitalio.DigitalInOut(board.GP12)
radio_signal.direction = digitalio.Direction.OUTPUT

cams        = []
current_cam = None
prev_cam    = None
override    = False

cams.append(Camera(board.GP22, board.GP1, 0, 1))
cams.append(Camera(board.GP21, board.GP2, 1, 1))
cams.append(Camera(board.GP20, board.GP5, 0, 0))
cams.append(Camera(board.GP19, board.GP6, 1, 0))

latch = Latch(board.GP18, board.GP9)


def toggleCam(cam):
    global current_cam

    if cam == current_cam:
        cam.deactivate()
        current_cam = None
        activateRadio(False)
    else:
        if not current_cam == None:
            current_cam.deactivate()
        cam.activate()
        current_cam = cam
        activateRadio(True)

def activateRadio(state):
    global radio_signal

    radio_signal.value = state

def reverseScan():
    global rev_trigger, latch, prev_cam, override

    if rev_trigger.value and not override and latch.getStatus() and not current_cam == cams[0]:
        print("Activating Reverse Camera")
        prev_cam = current_cam
        override = True
        toggleCam(cams[0])
    elif override and not rev_trigger.value:
        print("Re-activating Previous Camera")
        if prev_cam:
            toggleCam(prev_cam)
        else:
            toggleCam(current_cam)
        prev_cam = None
        override = False

while True:
    latch.scan()

    reverseScan()

    for cam in cams:
        if cam.button_status():
            while cam.button_status():
                time.sleep(0.01)
            print("Camera Button Press")
            toggleCam(cam)
            time.sleep(0.1)

    time.sleep(0.001)
