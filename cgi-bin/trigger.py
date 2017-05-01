#!/usr/bin/python
print "Content-type:text/html\n"

from subprocess import call
import cgi

form = cgi.FieldStorage() #Gets the full CGI script of "FieldStorage(None, None, [MiniFieldStorage('time', '12:40')])"
form = form.value[0] #strips only the value of the input to "MiniFieldStorage('time', '12:40')" because the value is a list
form = form.value #gets only the time because asks for value inside of the value "12:40"

alarmHour = form[:2]
alarmMinute = form[-2:]

call(["sudo","python","cgi-bin/alarm.py",str(alarmHour),str(alarmMinute)])