from .loader import *

class Player(Singleton):
    fields = ['midi_device_number']
    midi_device_num_choices = list(MIDI_OUTPUTS)
    midi_device_number = midi_device_num_choices[1] \
        if midi_device_num_choices else None
    def setup(self):
        self.midi_output = MIDI_OUTPUTS[self.midi_device_number]
    def play(self, piece):
        print(f'Playing smth on {self.midi_output}')
