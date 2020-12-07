from .loader import *

from .player import *

class Application(QApplication):
    def setup(self):
        self.adapt(Player(), name='player')
        super().setup()

class SomeLabel(QLabel):
    text = 'Lorem ipsum'

class Timer(QLabel):
    text = 'lorem ipsum'
    def update(self):
        self.text = str(round(self.player_thread_adapter.time, 2))
        super().update()
    @property
    def player_thread_adapter(self):
        return self._PlayerThreadAdapter.object()

class PlayOrStopButton(QPushButton):
    text = 'Play'
    def update(self):
        self.text = {True: 'Play', False: 'Stop'}.get(
            self.player.thread_adapter.waiting)
        super().update()
    def action(self):
        self.player.toggle_activity()
        self.update()
        self._Timer.object().update()
    @property
    def player(self):
        return self._Player.object()

class MainWidget(QWidget):
    widgets = [
        'SomeLabel',
        'Timer',
        'PlayOrStopButton'
    ]
