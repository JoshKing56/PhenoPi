from picamera import PiCamera
from time import sleep
from datetime import datetime
import yaml
import os
import multiCameraCapture

waitTime = 2
remoteName = "gdrive"

def setupLocalDir(parentDir, timeStamp):
    print(parentDir)
    if not os.path.exists(parentDir):
        print("Parent directory not found")
        return()
    else:
        fullPath = parentDir + "/" + timeStamp
        if not os.path.exists(fullPath):
            os.makedirs(fullPath)
            return(fullPath + "/")

# THIS IS THE VERSION OF THE FUNCTION I KNOW WORKS. REMOVE AFTER TESTING
# def takePicture(outDirectory, timeStamp):
#     picam = PiCamera()
#     outFile = outDirectory + timeStamp + ".png"
#     picam.start_preview()
#     # TODO: Document this behavior: need to sleep for at least two seconds to make sure sensors adjust
#     # TODO: pass this value as a param
#     sleep(waitTime)
#     picam.capture(outFile)
#     picam.stop_preview()
#     picam = None
#     return outFile

def takePicture(outDirectory):
    for cameraNum in range(1,5):
        picam = PiCamera()
        outFile = outDirectory + "camera" + str(cameraNum) + ".png"
        multiCameraCapture.switchCamera(cameraNum)
        picam.start_preview()
        sleep(waitTime)
        picam.capture(outFile)
        picam.stop_preview()
        picam.close()

def generateMetaData(metadata, timeStamp, filename):
    metadata["Picture taken"] = timeStamp
    with open(filename, 'w') as outfile:
        yaml.dump(metadata, outfile, default_flow_style=False)


def uploadData(source, dest):
    rclone = "rclone copy " + source + " " + remoteName + ":" + dest
    os.system(rclone)


def captureImage(metadata):
    timeStamp = str(datetime.now().strftime('%Y-%m-%d_%H_%M_%S'))
    print(timeStamp)

    localDir = setupLocalDir("/home/pi/Pictures/plant_data", timeStamp)
    infoPath = localDir + 'info.yml'
    generateMetaData(metadata, timeStamp, infoPath)
    takePicture(localDir)

    remoteDir = "Phenotyping/plant_data/" + timeStamp
    uploadData(localDir, remoteDir)
    return(True) #TODO: Improve this
    
