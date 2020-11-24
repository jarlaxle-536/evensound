from .loader import *

class Instrument(Entity):

    program_code = 1
    fields = [
        'program_code',
    ]
    midi_codes = MIDI_CODES.copy()

    @property
    def name(self):
        return MIDI_CODES_FLATTENED.get(str(self.program_code))

    @staticmethod
    def find_program_code_by_name(name):
        return (lambda l: int(l[0]) if l else None)(
            [k for k, v in MIDI_CODES_FLATTENED.items() if v == name])

    def __str__(self):
        return f'{self.name}'
