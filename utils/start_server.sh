until exec 6<>/dev/tcp/127.0.0.1/5000 &> /dev/null
do
	sleep 0.1
	echo "waiting"
done

# chromium-browser --kiosk "127.0.0.1:5000"
chromium-browser "127.0.0.1:5000"
