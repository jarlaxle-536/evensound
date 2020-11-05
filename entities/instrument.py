from auxiliary import *
from data_loader import *
from config import *

class Instrument(Root):
    fields = [
        'type',
        'code',
    ]
    instrument_timbre_choices = list(zip(*
        (lambda l: [list(range(1, len(l) + 1)), l])
        (list(MIDI_CODES.keys()))
    ))
    instrument_timbre = instrument_timbre_choices[0][0]
    instrument_code_choices = [(int(k), v) for k, v in MIDI_CODES_FLATTENED.items()]
    instrument_code = instrument_code_choices[0][0]
    def setup(self):
        print(self.instrument_timbre_choices)
    @property
    def name_expanded(self):
        return MIDI_CODES_FLATTENED.get(str(self.instrument_code), None)
