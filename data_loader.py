import json
import os

from config import *

midi_codes_filepath = os.path.join(DATA_DIR, 'midi_codes.json')
with open(midi_codes_filepath) as file:
    MIDI_CODES = json.load(file)
MIDI_CODES_FLATTENED = dict()
for k, v in MIDI_CODES.items():
    MIDI_CODES_FLATTENED.update(v)
MIDI_CODES_FLATTENED_INVERSE = {v: k for k, v in MIDI_CODES_FLATTENED.items()}

# NOTES, SCALES, etc

with open(NOTES_FILEPATH) as file:
    NOTES = json.load(file)
