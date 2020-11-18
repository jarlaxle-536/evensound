from .general import *

from scripts.detect_midi_outputs import *

class MidiOutput(Singleton):
    fields = ['device_number']
    device_num_choices = detect_midi_outputs()
    device_number = device_num_choices[0] if device_num_choices else None
    def setup(self):
        print(self.device_number, type(self.device_number))
        self.output = pygame.midi.Output(self.device_number)
    def __str__(self):
        return f'<MidiOutput: {pygame.midi.get_device_info(self.device_number)}>'
