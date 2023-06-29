# Make sure that the simulator is running and has been set up before executing this script
# Sample from https://github.com/MrYsLab/PyMata/blob/master/examples/piezo/piezo_beep.py

import time
import sys
import signal

from pymata.pymata import PyMata

BEEPER = 3  # pin that piezo device is attached to

# create a PyMata instance
board = PyMata("tcp://localhost:5555")

def signal_handler(sig, frm):
    print('You pressed Ctrl+C!!!!')
    if board is not None:
        board.reset()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

board.play_tone(BEEPER, board.TONE_TONE, 1000, 500)
time.sleep(2)

# play a continuous tone, wait 3 seconds and then turn tone off
board.play_tone(BEEPER, board.TONE_TONE, 1000, 0)
time.sleep(3)
board.play_tone(BEEPER, board.TONE_NO_TONE, 1000, 0)

board.close()