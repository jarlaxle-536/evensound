from logic.loader import *

class Player(Singleton):
    def setup(self):
        self.adapt(self._PlayerThreadAdapter(), name='thread_adapter')
    @property
    def playing(self):
        return not self.thread_adapter.waiting

class PlayerThreadAdapter(QtThreadAdapter):
    _fields = ['time', 'waiting']
    time = 0
    period = 0.05
    def action(self):
        super().action()
        self.time += self.period
    def toggle_activity(self):
        print(f'toggling {self}')
        super().toggle_activity()
