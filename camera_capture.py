import os
running_on_pi = True
CAMERA_WAIT_TIME = 2

try:
    from picamera import PiCamera
    import RPi.GPIO as gp
except ImportError:
    running_on_pi = False
    print("Detected that this is not running from a RaspberryPi")

if (running_on_pi):
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

def takePicture(outDirectory):
    if (running_on_pi):
        for cameraNum in range(1,4):
            outFile = outDirectory + "camera" + str(cameraNum) + ".png"
            switchCamera(cameraNum)
            with PiCamera() as picam:
                picam.start_preview()
                sleep(CAMERA_WAIT_TIME)
                picam.stop_preview()
                picam.capture(outFile)
    else:
        print("Assuming camera hardware works...")