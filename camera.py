from picamera import PiCamera
from time import sleep

camera = PiCamera()

def captureImage(waitTime, savePath):
    camera.start_preview()
    # need to sleep for at least two seconds to make sure sensors adjust
    # TODO: test to see if this is right
    # TODO: pass this value as a param
    sleep(waitTime)
    camera.capture(savePath)
    camera.stop_preview()

for i in range(10):
    captureImage(i, "/home/pi/Pictures/plant_data/%s.png" % i)

