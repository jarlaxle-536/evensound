import json
import os

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(MAIN_DIR, 'data')

midi_codes_filepath = os.path.join(DATA_DIR, 'midi_codes.json')
with open(midi_codes_filepath) as file:
    midi_codes = json.load(file)
