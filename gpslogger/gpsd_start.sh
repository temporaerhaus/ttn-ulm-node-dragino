#!/bin/sh
sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock
sleep 5
python /home/pi/geosender/gpslogger/gps.py

