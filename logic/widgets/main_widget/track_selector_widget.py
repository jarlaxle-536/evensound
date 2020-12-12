from logic.loader import *

class TrackSelectorWidget(QListWidget):
    _fields = ['selected']
    def update(self):
        self._entities = self._Composition.object().tracks.contents
        super().update()
