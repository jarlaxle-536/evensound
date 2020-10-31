from config import *
from data_loader import *
from .general import *

class Instrument(Entity):
    fields = [
        'instrument_code',
    ]
    choices = [(int(k), v) for k, v in MIDI_CODES_FLATTENED.items()]
    instrument_code = choices[0][0]
    @property
    def name_expanded(self):
        return MIDI_CODES_FLATTENED.get(str(self.instrument_code), None)
