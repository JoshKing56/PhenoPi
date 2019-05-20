#from picamera import PiCamera
from time import sleep
from datetime import datetime

#camera = PiCamera()

waitTime = 2
outDirectory =  "plant_data/"

def setupDirectory(parentDir):
    if(os.path.exists(parentDir)):
        print("Parent directory not found")
        return()
    else:
        print("got here")
        #timeStamp = str(datetime.now()) #TODO: Make this better for capturing
        print(timeStamp)
        fullPath = parentDir + "/" timeStamp
        if not os.path.exists(fullPath):
            os.makedirs(parentDir + "/" timeStamp)
            return(parentDir + "/" timeStamp)

def captureImage():
    outFile = outDirectory + timeStamp + ".png"
    camera.start_preview()
    # need to sleep for at least two seconds to make sure sensors adjust
    # TODO: test to see if this is right
    # TODO: pass this value as a param
    sleep(waitTime)
    camera.capture(outDirectory)
    camera.stop_preview()

setupDirectory("/home/josh/Pictures/phenopi/")
#captureImage()
