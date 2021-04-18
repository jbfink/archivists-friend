# this is needed for circuitpython itself to write to board
# taken from https://learn.adafruit.com/cpu-temperature-logging-with-circuit-python/writing-to-the-filesystem , adapted to magtag. D15 is leftmost button - hold it down while resetting/plugging in board to enable on-board write to filesystem.

import storage     
import digitalio
import board
switch = digitalio.DigitalInOut(board.D15)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP
storage.remount("/", switch.value)
