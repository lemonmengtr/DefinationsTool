#!/bin/bash
while true
do 
    hour=`date +%H`
    if [ $hour == "01" ]
    then
        ./runnow.sh >> log.txt
    fi
    date +%H:%M:%S >> log.txt
    sleep 600
done





