from logic.loader import *

class Instrument(Entity):
    code = "1"
    @property
    def name(self):
        return MIDI_CODES_FLATTENED.get(self.code, '')
    def __str__(self):
        return self.name

midi_codes_filepath = os.path.join(DATA_DIR, 'midi_codes.json')
with open(midi_codes_filepath) as file:
    MIDI_CODES = json.load(file)
MIDI_CODES_FLATTENED = dict()
for k, v in MIDI_CODES.items():
    MIDI_CODES_FLATTENED.update(v)
MIDI_CODES_FLATTENED_INVERSE = {v: k for k, v in MIDI_CODES_FLATTENED.items()}
