from picamera import PiCamera
from time import sleep
from datetime import datetime
import yaml
import os

camera = PiCamera()

waitTime = 2
remoteName = "gdrive"

user = "Josh"
species = "Barley"
plant = 5

def setupLocalDir(parentDir, timeStamp):
    print(parentDir)
    if not os.path.exists(parentDir):
        print("Parent directory not found")
        return()
    else:
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
    return outFile

def generateMetaData(timeStamp, filename):
    output = {'User': user, "Plant species": species, "Plant Number": plant, "Picture taken": timeStamp}
    with open(filename, 'w') as outfile:
    yaml.dump(output, outfile, default_flow_style=False)

def uploadData(fileName, remoteDirectory):
   os.system("rclone copy {file}, {remote}:{remoteDir}".format(file=fileName, remote=remoteName, remoteDir=remoteDirectory))

outDirectory = "/home/pi/Pictures/plant_data"
timeStamp = str(datetime.now().strftime('%Y-%m-%d_%H_%M_%S')) #TODO: Make this better for capturing

setupLocalDir(outDirectory, timeStamp)
generateMetaData(timeStamp, 'info.yml')
infoPath = outDirectory + 'info.yml'
imagePath = outDirectory + captureImage()

uploadData(imageName, timeStamp)
uploadData(infoPath, timeStamp)

#captureImage()
