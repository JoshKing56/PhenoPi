# Do not touch these variables!

PROJROOT "~/Documents/PhenoPi"

# Check for any updates

function sync_with_github{
	cd $PROJROOT
	if git pull;
		echo "project synced with remote"
	else
		echo "ERROR: UNABLE TO UPDATE PROJECT. PLEASE FIX"
	fi
}

if [ -d "$PROJROOT"]
	sync_with_github	
else
	echo "ERROR: PROJECT DIRECTORY NOT FOUND. PLEASE FIX"
fi

cd $PROJROOT

python3 display.py 
bash start_server.sh 2&>1 /dev/null
