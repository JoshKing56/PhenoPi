# PhenoPi
## What is this?
This repo contains all of the code that makes the PhenoPi phenotyping rig work. It has several components:
1. Code for the python application on the raspberry pi
2. Recieving end code for the host machine

## Dependencies
The following are dependencies for this project:
### Python #TODO: See if I can use python 3.6
* Flask
* picamera
* pyyaml
* wtf-flask
* wtforms


## Setting up the pi
### Enable camera
In order to enable the camera, you need to open /boot/config.txt in a text editor (with sudo) and make sure the following lines look like this:

```
start_x=1             # essential
gpu_mem=128           # at least, or maybe more if you wish
disable_camera_led=1  # optional, if you don't want the led to glow
```
#TODO: Automate this
You can also just use the raspi-config utility. 

## Camera
The camera uses the standard picamera python library

## Bash scripts
These bash scripts automate things around booting the raspberry pi. Things it does:
* Update the code automatically from github
* start the gui

## Syncing with remote
For now, the way files are managed is through Google drive. After creating a remote using rclone, we can upload a file thoruhg
`rclone copy [file] gdrive:/Phenotyping/plant_data`
While there is a package in Python, for now the python script just use os.system()

# Resources

https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/5
https://picamera.readthedocs.io/en/release-1.13/
https://stackoverflow.com/questions/36283347/raspberry-pi-camera-out-of-resources
https://pypi.org/project/piexif/
https://python-xmp-toolkit.readthedocs.io/en/latest/using.html
