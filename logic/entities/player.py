from logic.loader import *

class Player(Singleton):
    _fields = ['waiting', 'output']
    def setup(self):
        self.adapt(PlayerThreadAdapter(), name='thread_adapter')
        self.waiting = self.thread_adapter.waiting
    def __str__(self):
        return f'<PLAYER output={self.output} waiting={self.waiting}>'

class PlayerThreadAdapter(QtThreadAdapter):
    time = 0
    period = 1
    def action(self):
        super().action()
        self.time += self.period
    def toggle_activity(self):
        print(f'toggling {self}')
        super().toggle_activity()
