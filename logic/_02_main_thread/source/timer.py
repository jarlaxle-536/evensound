from .loader import *

class Timer(QLabel):
    text = 'lorem ipsum'
    def update(self):
        self.text = str(round(self.player_thread_adapter.time, 2))
        super().update()
    @property
    def player_thread_adapter(self):
        return self._PlayerThreadAdapter.object()
