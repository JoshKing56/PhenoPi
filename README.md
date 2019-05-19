# PhenoPi
## What is this?
This repo contains all of the code that makes the PhenoPi phenotyping rig work. It has several components:
1. Code for the python application on the raspberry pi
2. Recieving end code for the host machine

## Camera
The camera uses the standard picamera python library

## Bash scripts
These bash scripts automate things around booting the raspberry pi. Things it does:
* Update the code automatically from github
* start the gui