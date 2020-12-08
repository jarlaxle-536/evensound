from logic.loader import *

class PlayOrStopButton(QPushButton):
    _subscriptions = {
        ('PlayerThreadAdapter', 'waiting')
    }
    def update(self):
        self.text = self.get_text()
        super().update()
    @property
    def player(self):
        return self._Player.object()
    def get_text(self):
        return {True: 'Stop', False: 'Play'}.get(
            self.player.playing)
    def action(self):
        super().action()
        self.player.toggle_activity()
