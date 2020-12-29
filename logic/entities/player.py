from logic.loader import *

from logic.functions import *
from .midi_output import *

class Player(Singleton):
    _fields = ['waiting', 'midi_output']
    def setup(self):
        self.adapt(PlayerThreadAdapter(), name='thread_adapter')
        self.waiting = self.thread_adapter.waiting
        self.initialize_midi_outputs()
    def initialize_midi_outputs(self):
        self.adapt(MIDIOutputContainer(), name='midi_outputs')
        for midi_output_data in detect_midi_outputs():
            self.midi_outputs.insert(MIDIOutput(**midi_output_data))
        self.midi_output = (lambda l: l[0] if l else None)(self.midi_outputs)
    def __str__(self):
        return f'<PLAYER output={self.midi_output} waiting={self.waiting}>'

class PlayerThreadAdapter(QtThreadAdapter):
    time = 0
    period = 1
    def action(self):
        super().action()
        self.time += self.period
