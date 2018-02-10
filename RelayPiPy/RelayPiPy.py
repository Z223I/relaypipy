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

    pinList = []
########################################################
# method __init__
########################################################

    def __init__(self):
#        print "__init__"
  
        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)
# End method __init__


########################################################
# Method init
# This method is to be called only once.  It should be
# called by the main program.
#
# All other instances will access the class attribute
# pinList.
########################################################

    def init(self, _pinList):
#        print "init"
        RelayPiPy.pinList = _pinList
#        print _pinList
#        time.sleep(2)


        for i in RelayPiPy.pinList:
#            print i
            GPIO.setup(i, GPIO.OUT, initial=1) 
#            time.sleep(2)

# End method init


########################################################
# method off
########################################################

    def off(self, _relay):
#        print "off"
        pin = RelayPiPy.pinList[_relay]
        GPIO.output(pin, GPIO.HIGH)

# End method off


########################################################
# method on
########################################################

    def on(self, _relay):
#        print "on"
        pin = RelayPiPy.pinList[_relay]
        GPIO.output(pin, GPIO.LOW)

# End method on


########################################################
# method setAllPins
#
# Input state should be set to GPIO.LOW or GPIO.HIGH
########################################################

    def setAllPins(self, state):
#        print "setAllPins"
        for pin in RelayPiPy.pinList: 
            GPIO.output(pin, state) 

# End method setAllPins



########################################################
# method shutdown
########################################################

    def shutdown(self):
#        print "shutdown"
        GPIO.cleanup()
# End method shutdown




########################################################
# method test1
########################################################

    def test1(self):
#        print "test1"

        self.setAllPins(GPIO.HIGH)

        relay = 0
        state = GPIO.LOW
        timeSleep = 1

        for pin in RelayPiPy.pinList: 
            GPIO.output(pin, state)
            relay += 1
            print(relay)
            time.sleep(timeSleep)

# End method test1

########################################################
#
# End class RelayPiPy
#
########################################################
