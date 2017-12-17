#!/usr/bin/python
#


# This work was built upon https://github.com/skiwithpete/relaypi


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
#        print "__init__"
  
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)

        self.pins = []
# End Function __init__


########################################################
# Function init
########################################################

    def init(self, _pinList):
#        print "init"
        self.pinList = _pinList
        for i in self.pinList: 
            GPIO.setup(i, GPIO.OUT) 

# End Function init


########################################################
# Function off
########################################################

    def off(self, _relay):
#        print "off"
        pin = self.pinList[_relay]
        GPIO.output(pin, GPIO.LOW)

# End Function off


########################################################
# Function on
########################################################

    def on(self, _relay):
#        print "on"
        pin = self.pinList[_relay]
        GPIO.output(pin, GPIO.HIGH)

# End Function on


########################################################
# Function setAllPins
#
# Input state should be set to GPIO.LOW or GPIO.HIGH
########################################################

    def setAllPins(self, state):
#        print "setAllPins"
        for pin in self.pinList: 
            GPIO.output(pin, state) 

# End Function setAllPins



########################################################
# Function shutdown
########################################################

    def shutdown(self):
#        print "shutdown"
        GPIO.cleanup()
# End method shutdown




########################################################
# Function test1
########################################################

    def test1(self):
#        print "test1"

        self.setAllPins(GPIO.HIGH)

        relay = 0
        state = GPIO.LOW
        timeSleep = .5

        for pin in self.pinList: 
            GPIO.output(pin, state)
            relay += 1
            print relay
            time.sleep(timeSleep)

# End Function test1

########################################################
#
# End class RelayPiPy
#
########################################################
