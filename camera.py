from picamera import PiCamera
from time import sleep

def captureImage(waitTime, savePath):
    camera = PiCamera()

    camera.start_preview()
    # need to sleep for at least two seconds to make sure sensors adjust
    # TODO: test to see if this is right
    # TODO: pass this value as a param
    sleep(waitTime)
    camera.capture(savePath)
    camera.stop_preview()

captureImage(2, "/home/pi/Pictures/plant_data/test.png")
