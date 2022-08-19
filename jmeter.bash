for i in {1..3}
do
	echo "+++start to sleep++++"
	sleep 10
	echo "+++waking up++++"
	~/apache-jmeter-5.5/bin/jmeter -n -t ~/apache-jmeter-5.5/$1.jmx
done
echo "$SECONDS seconds"
