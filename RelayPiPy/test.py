#!/usr/bin/python
#
import time
import RPi.GPIO as GPIO
from RelayPiPy import RelayPiPy

relay4 = RelayPiPy()



# init list with pin numbers
pinList = [6, 13, 19, 26]
relay4.init(pinList)


try:

  # Don't understand it but, GPIO.LOW is apparently ON
  # skiwithpete@github used reverse logic also.
  relay4.setAllPins(GPIO.LOW)
  time.sleep(1)

  for relay in range(4):
    relay4.off(relay)
    time.sleep(1)

  for relay in range(4):
    relay4.on(relay)
    time.sleep(1)

  relay4.setAllPins(GPIO.HIGH)
  time.sleep(2)

  relay4.test1()

  relay4.shutdown()
  print("Good bye!")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print("Quit")

  # Reset GPIO settings
  GPIO.cleanup()
