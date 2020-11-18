from .general import *

from .midi_output import *

class Player(Singleton):
    def setup(self):
        self.midi_output = MidiOutput()
    def play(self, piece):
        print(f'Playing smth on {self.midi_output}')
