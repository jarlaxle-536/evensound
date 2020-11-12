from auxiliary import *
from data_loader import *
from config import *

class Instrument(Root):
    fields = [
        'type',
        'code',
    ]
    instrument_timbre_choices = list(MIDI_CODES.keys())
    instrument_timbre = instrument_timbre_choices[0]
    instrument_code_choices = list(MIDI_CODES[instrument_timbre].values())
    instrument_code = instrument_code_choices[0]
    def setup(self):
        pass
    @property
    def name_expanded(self):
        return MIDI_CODES_FLATTENED.get(str(self.instrument_code), None)
