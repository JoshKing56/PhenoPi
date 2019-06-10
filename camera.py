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

def takePicture(outDirectory):
    for cameraNum in range(1,5):
        outFile = outDirectory + "camera" + str(cameraNum) + ".png"
        multiCameraCapture.switchCamera(cameraNum)
        picam = PiCamera()
        picam.start_preview()
        sleep(waitTime)
        picam.stop_preview()
        picam.capture(outFile)
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

    remoteDir = "Phenotyping/plant_data/" + metadata['Experiment Number'] + "/" + timeStamp
    uploadData(localDir, remoteDir)
    return(True)     
