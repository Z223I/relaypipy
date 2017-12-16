#!/usr/bin/python
#


# Import required libraries
import time
import RPi.GPIO as GPIO




########################################################
#
# Class RelayPiPy
#
# This class manipulates relay(s).
#
########################################################

class RelayPiPy():


########################################################
# Function __init__
########################################################

    def __init__(self):
        print "__init__"
  
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)

        self.pins = []
# End Function __init__


########################################################
# Function init
########################################################

    def init(self):
        print "init"

        # Set pins to output and initialize them to false.
#    GPIO.setup(self.powerLockPinA, GPIO.OUT)
#    GPIO.output(self.powerLockPinA, False)
#    GPIO.setup(self.powerLockPinB, GPIO.OUT)
#    GPIO.output(self.powerLockPinB, False)

# End Function init

########################################################
#
# End class RelayPiPy
#
########################################################

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [6, 13, 19, 26]

# loop through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
  GPIO.output(6, GPIO.LOW)
  print "ONE"
  time.sleep(SleepTimeL); 
  GPIO.output(13, GPIO.LOW)
  print "TWO"
  time.sleep(SleepTimeL);  
  GPIO.output(19, GPIO.LOW)
  print "THREE"
  time.sleep(SleepTimeL);
  GPIO.output(26, GPIO.LOW)
  print "FOUR"
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/WpM1aq4B8-A
