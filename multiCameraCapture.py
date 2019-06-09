import RPi.GPIO as gp
import os

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.output(7, False)
gp.output(11, False)
gp.output(12, True)

def switchCamera(camera):
    if (camera == 1):
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)

    elif (camera == 2):
        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)

    elif (camera == 3):
        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)

    elif (camera == 4):
        gp.output(7, True)
        gp.output(11, True)
        gp.output(12, False)
