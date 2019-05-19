# PhenoPi
## What is this?
This repo contains all of the code that makes the PhenoPi phenotyping rig work. It has several components:
1. Code for the python application on the raspberry pi
2. Recieving end code for the host machine

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
