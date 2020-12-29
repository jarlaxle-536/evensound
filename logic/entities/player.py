from logic.loader import *

from logic.functions import *
from .midi_output import *
from .cursor import *

class Player(Singleton):
    _fields = ['time', 'waiting', 'midi_output', 'speed']
    time = 0
    speed = 1
    def setup(self):
        self.adapt(PlayerThreadAdapter(), name='thread_adapter')
        self.adapt(Cursor(), name='cursor')
#        self.waiting = self.thread_adapter.waiting
        self.initialize_midi_outputs()
    def set_speed(self, speed_level):
        print(f'{self}:set_speed {speed_level}')
        self.speed = speed_level
        self.thread_adapter.waiting = speed_level == 0
        print(f'{self} TA waiting:', self.thread_adapter.waiting)
    def initialize_midi_outputs(self):
        self.adapt(MIDIOutputContainer(), name='midi_outputs')
        for midi_output_data in detect_midi_outputs():
            self.midi_outputs.insert(MIDIOutput(**midi_output_data))
        self.midi_output = (lambda l: l[0] if l else None)(self.midi_outputs)
    def __str__(self):
        return f'<PLAYER time={round(self.time, 1)} output={self.midi_output} adapter={self.thread_adapter}>'

class PlayerThreadAdapter(QtThreadAdapter):
    _dependent_on = ['Note']
    period = 0.1
    def update(self):
        super().update()
        try:
            current_bar = self._Composition.object().bars[0]
            print(current_bar.duration)
            self.commands = current_bar.get_commands_list()
        except Exception:
            self.commands = list()
    def action(self):
        super().action()
        print(f'{self} commands: {self.commands}')
        current_bar = self._Composition.object().bars[0]
        print(f'current bar: {current_bar}, duration: {current_bar.duration}')
        while self.commands:
            cmd_time, cmd = heapq.heappop(self.commands)
            if cmd_time > self.adapter.time:
                heapq.heappush(self.commands, (cmd_time, cmd))
                break
            print('will execute:', cmd_time, cmd)
            cmd.execute()
        self.adapter.time += self.period
        print(self.adapter.time)
    def __str__(self):
        return f'<PlayerTA waiting={self.waiting}>'

Player()
