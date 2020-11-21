from .loader import *

class Player(Singleton):
    fields = ['midi_device_number']
    midi_outputs = MIDI_OUTPUTS.copy()
    midi_device_number = list(midi_outputs)[0]
    def update(self):
        self.midi_output = self.midi_outputs[self.midi_device_number]
    def setup(self):
        self.update()
    def play(self, piece):
        print(f'Playing smth on {self.midi_output}')

class MidiOutput(Entity):
    pass
