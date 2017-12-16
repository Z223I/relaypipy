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

    def init(self, _pinList):
        print "init"
        self.pinList = _pinList
        for i in pinList: 
            GPIO.setup(i, GPIO.OUT) 

        # Set pins to output and initialize them to false.
#    GPIO.setup(self.powerLockPinA, GPIO.OUT)
#    GPIO.output(self.powerLockPinA, False)
#    GPIO.setup(self.powerLockPinB, GPIO.OUT)
#    GPIO.output(self.powerLockPinB, False)

# End Function init


########################################################
# Function init
#
# state should be set to GPIO.LOW or GPIO.HIGH
########################################################

    def setAllPins(self, state):
        print "setAllPins"
        for i in pinList: 
            GPIO.output(i, state) 

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


relay4 = RelayPiPy()


# init list with pin numbers
pinList = [6, 13, 19, 26]
relay4.init(pinList)

relay4.setAllPins(GPIO.HIGH)

print "..."
print





GPIO.setmode(GPIO.BCM)

# loop through pins and set mode and state to 'high'
for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = .1

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
