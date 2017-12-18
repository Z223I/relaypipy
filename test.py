#!/usr/bin/python
#
import time
import RPi.GPIO as GPIO
from relaypipy import RelayPiPy

relay4 = RelayPiPy()



# init list with pin numbers
pinList = [6, 13, 19, 26]
relay4.init(pinList)


try:

  if False == GPIO.LOW:
    print "False == GPIO.LOW"
  else:
    print "False != GPIO.LOW"

  relay4.setAllPins(GPIO.LOW)

  for relay in range(4):
    relay4.off

  for relay in range(4):
    relay4.on(relay)
    time.sleep(.2)

  relay4.setAllPins(GPIO.HIGH)
  

#  relay4.test1()

  relay4.shutdown()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()
