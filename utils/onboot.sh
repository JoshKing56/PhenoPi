#!/bin/bash

# Do not touch these variables!

PROJROOT="/home/pi/Documents/PhenoPi"

# Check for any updates

function sync_with_github {
	cd $PROJROOT
	if git pull;then
		echo "project synced with remote"
	else
		echo "ERROR: UNABLE TO UPDATE PROJECT. PLEASE FIX"
	fi
}

if [ -d "$PROJROOT" ];then
	sync_with_github	
else
	echo "ERROR: PROJECT DIRECTORY NOT FOUND. PLEASE FIX"
fi

cd $PROJROOT

python3 ~/Documents/PhenoPi/display.py &
bash start_server.sh 
