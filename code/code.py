import board
import digitalio
import time

from camera import Camera

cams = []
current_cam = None

cams.append(Camera(board.GP22, board.GP1))
cams.append(Camera(board.GP21, board.GP2))
cams.append(Camera(board.GP20, board.GP5))
cams.append(Camera(board.GP19, board.GP6))

while True:
    for cam in cams:
        if cam.button_status():
            while cam.button_status():
                time.sleep(0.001)
            print("BUTTON RELEASED")

    time.sleep(0.001)
