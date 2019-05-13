#!/usr/bin/python  
import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode(GPIO.BCM)  
  
# init list with pin numbers  
  
pinList = [2, 3, 4, 5, 6, 13, 16, 19, 20, 21, 26]  
  
# loop through pins and set mode and state to 'low'  
  
for i in pinList:   
  GPIO.setup(i, GPIO.OUT)   
  GPIO.output(i, GPIO.HIGH)  
  
# time to sleep between operations in the main loop  
  
SleepTimeL = 0.2  
  
# main loop  
  
try:  
  GPIO.output(26, GPIO.LOW)  
  print "Activating CIU screen..."  
  time.sleep(SleepTimeL);   
     
  GPIO.cleanup()
  print "Done!"  
  
# End program cleanly with keyboard  
except KeyboardInterrupt:  
  print " Exiting now ..."  
  
  # Reset GPIO settings  
  GPIO.cleanup()  
