from .loader import *

class Player(Singleton):
    def setup(self):
        self.adapt(PlayerThreadAdapter(), name='thread_adapter')

class PlayerThreadAdapter(QtThreadAdapter):
    _fields = ['time']
    time = 0
    period = 0.05
    def action(self):
        super().action()
        self.time += self.period
