#!/usr/bin/python
#
import RPi.GPIO as GPIO
from relaypipy import RelayPiPy

relay4 = RelayPiPy()


# init list with pin numbers
pinList = [6, 13, 19, 26]
relay4.init(pinList)


try:

  relay4.setAllPins(GPIO.LOW)

  relay4.test1()

  relay4.shutdown()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()
