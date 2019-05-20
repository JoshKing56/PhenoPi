#from picamera import PiCamera
from time import sleep
from datetime import datetime
import os

#camera = PiCamera()

waitTime = 2

def setupDirectory(parentDir):
    print(parentDir)
    if not os.path.exists(parentDir):
        print("Parent directory not found")
        return()
    else:
        timeStamp = str(datetime.now()) #TODO: Make this better for capturing
        fullPath = parentDir + "/" + timeStamp
        if not os.path.exists(fullPath):
            os.makedirs(fullPath)
            return(fullPath)

def captureImage():
    outFile = outDirectory + timeStamp + ".png"
    camera.start_preview()
    # need to sleep for at least two seconds to make sure sensors adjust
    # TODO: test to see if this is right
    # TODO: pass this value as a param
    sleep(waitTime)
    camera.capture(outDirectory)
    camera.stop_preview()

outDirectory = "/home/pi/Pictures/plant_data"
print(setupDirectory(outDirectory))
#captureImage()
