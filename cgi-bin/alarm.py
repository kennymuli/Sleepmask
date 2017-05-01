#!/usr/bin/python
print "Content-type:text/html\n"

import wiringpi2 as wiringpi
from time import sleep, strftime
from sys import argv

alarmHour = argv[1]
alarmMinute = argv[2]

	
alarmTime = alarmHour + ":" + alarmMinute
currentTime = strftime("%H:%M")

if alarmTime == currentTime:

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(14,1)
wiringpi.pinMode(16,1)

def ledOn():
	wiringpi.digitalWrite(14,1)
	wiringpi.digitalWrite(16,1)

def ledOff():
	wiringpi.digitalWrite(14,0)
	wiringpi.digitalWrite(16,0)

while True:
	currentTime = strftime("%H:%M")
	if currentTime == alarmTime:
		ledOn()
		break

sleep(30)
ledOff()

