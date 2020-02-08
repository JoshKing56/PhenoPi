from time import sleep
from datetime import datetime
import yaml
import os
import camera_capture 

remoteName = "gdrive"
image_storage_directory = os.environ['HOME'] + "/Pictures/plant_data"

def setupLocalDir(parentDir, timeStamp):
   fullPath = parentDir + "/" + timeStamp
    #try:
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
        return(fullPath + "/")
        
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

    localDir = setupLocalDir(image_storage_directory, timeStamp)
    infoPath = localDir + 'info.yml'
    generateMetaData(metadata, timeStamp, infoPath)
    takePicture(localDir)

    remoteDir = "Phenotyping/plant_data/" + metadata['Experiment Number'] + "/" + timeStamp
    uploadData(localDir, remoteDir)
    return(True)     
