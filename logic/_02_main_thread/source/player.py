from .loader import *

class Player(Singleton):
    def setup(self):
        self.adapt(PlayerThreadAdapter(), name='thread_adapter')

class PlayerThreadAdapter(QtThreadAdapter):
    time = 0
    period = 0.05
    def action(self):
        super().action()
        self.time += self.period

class PlayerTime(Singleton):
    value = 0
    def __add__(self, other):
        pass
