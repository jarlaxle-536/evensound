from logic.loader import *

class Instrument(Entity):
    code = "1"
    @property
    def name(self):
        return MIDI_CODES_FLATTENED.get(self.code, '')
    def __str__(self):
        return self.name
