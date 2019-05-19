from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

waitTime = 2
outDirectory =  "/home/pi/Pictures/plant_data/"

def captureImage():
    timeStamp = str(datetime.now()) #TODO: Make this better for capturing
    outFile = outDirectory + timeStamp + ".png"
    camera.start_preview()
    # need to sleep for at least two seconds to make sure sensors adjust
    # TODO: test to see if this is right
    # TODO: pass this value as a param
    sleep(waitTime)
    camera.capture(outDirectory)
    camera.stop_preview()

captureImage()