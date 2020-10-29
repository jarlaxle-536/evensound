import json

from config import *
from .general import *

class Instrument(Entity):
    fields = [
        'instrument_code',
    ]
    instrument_code = 1
    @property
    def name_expanded(self):
        return midi_codes.get(str(self.instrument_code), None)

midi_codes_filepath = os.path.join(DATA_DIR, 'midi_codes.json')
with open(midi_codes_filepath) as file:
    midi_codes = json.load(file)
