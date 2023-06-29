# Make sure that the simulator is running and has been set up before executing this script
# Sample from https://github.com/MrYsLab/PyMata/blob/master/examples/pymata_blink.py

import time
import sys
import signal

from pymata.pymata import PyMata

# Digital pin 13 is connected to an LED. If you are running this script with
# an Arduino UNO no LED is needed (Pin 13 is connected to an internal LED).
BOARD_LED = 13

# Create a PyMata instance
board = PyMata("tcp://localhost:5555", verbose=True)

# Set digital pin 13 to be an output port
board.set_pin_mode(BOARD_LED, board.OUTPUT, board.DIGITAL)

time.sleep(2)
print("Blinking LED on pin 13 for 10 times ...")

# Blink for 10 times
for x in range(10):
    print(x + 1)
    print("Writing High")

    # Set the output to 1 = High
    board.digital_write(BOARD_LED, 1)
    # Wait a half second between toggles.
    time.sleep(.5)
    # Set the output to 0 = Low
    print("Writing low")
    board.digital_write(BOARD_LED, 0)
    time.sleep(.5)

# Close PyMata when we are done
board.close()