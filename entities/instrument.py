from .general import *

class Instrument(Entity):
    program_code = 1
    fields = [
        'program_code',
    ]
    midi_codes = MIDI_CODES.copy()
    @property
    def name(self):
        return MIDI_CODES_FLATTENED.get(str(self.program_code))
    def setup(self):
        pass
    @staticmethod
    def get_id(dct):
        return dct.get('name')
