import mido
import rtmidi

all_output_names = mido.get_output_names()
for output_name in all_output_names:
    print(output_name)
    output = mido.open_output(output_name)
    output.send(mido.Message('note_on', note=72))

import time
from collections import deque

port_name = mido.get_output_names()[0]

msg = mido.Message('note_on', note=72)

output = rtmidi.MidiOut()
output.send_message([176, 0, 123])
print(dir(output))

import sys

for port in mido.get_output_names():
    if port.startswith('f_midi'):
        out = mido.open_output(port)
        break
else:
  print('ERROR: failed to find a port')
  sys.exit(1)

out.send(mido.Message('control_change', channel=0, control=0, value=123))
