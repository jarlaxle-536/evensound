from config import *
from .general import *

class Instrument(Entity):
    fields = [
        'instrument_code',
    ]
    choices = [(int(k), v) for k, v in midi_codes.items()]
    instrument_code = choices[0][0]
    @property
    def name_expanded(self):
        return midi_codes.get(str(self.instrument_code), None)
