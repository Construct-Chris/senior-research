#!/bin/bash

if [ -z "${1}" ] || [ -z "${2}" ]; then
  echo "the name of output file is missed"
  exit
fi
PWRFILE="temp-data"
WAIT_TIME=120
MSRE_TIME=240

powerstat 1 1000 -d $WAIT_TIME  -n > $PWRFILE  &

PSID=$(expr $$ + 1 )

TIMERS=("-" "|")
j=0
for (( j=1 ; j <= $WAIT_TIME ; j++ ))
do
	INDX=$(expr $j % 2)
	echo -n -e "\rWaiting for $j sec ${TIMERS[$INDX]}"
        sleep 1.08
done
echo
echo "-+-+-+-+  Start now  +-+-+-+-"
END=$(expr $MSRE_TIME + 8 )

bash jmeter.bash $2 > jmt.txt &
echo "Jmeter has started"
for (( c=1; c<=$MSRE_TIME; c++ ))
do
	INDX=$(expr $j % 2)
	echo -n -e "\rCollecting Power Consumption for $c sec ${TIMERS[$INDX]}"
        sleep 1
done

kill $PSID
sleep 1

echo
echo "-+-+-+-+  Finished, now converting to CSV  +-+-+-+-"

cat $PWRFILE | tr -s '[:blank:]' ',' | sed '/^[a-zA-Z,-\ ]/d' | sed "1d" > $1.csv
rm $PWRFILE

echo
echo "-+-+-+-+  Done  +-+-+-+-"
