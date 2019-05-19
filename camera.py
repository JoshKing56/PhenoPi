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

for i in range(1, 10, 0.5):
    captureImage(i, "/home/pi/Pictures/plant_data/%s.png" % i)
    
