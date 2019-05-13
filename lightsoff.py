#!/usr/bin/python  
import RPi.GPIO as GPIO  
import time
import sys
  
GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)
# init list with pin numbers  
  
pinList = [2, 3, 4, 5, 6, 13, 16, 19, 20, 21, 26]  
  
# loop through pins and set mode and state to 'low'  
  
for i in pinList:   
  GPIO.setup(i, GPIO.OUT)   
  GPIO.output(i, GPIO.HIGH)  
  
# time to sleep between operations in the main loop  
  
SleepTimeL = 10  
  
# main loop  
  
try:  
  GPIO.output(13, GPIO.HIGH)  
  print "Lights Turned OFF"  
  #time.sleep(SleepTimeL);   
     
  print "Good bye!"

except:
  pass
  sys.exit(1)

#GPIO.cleanup()  # Reset GPIO settings 
 

  
   
 
