from logic.loader import *

class TrackSelector(Singleton):
    _dependent_on = ['TrackListWidget']
    _fields = ['selected']

class TrackListWidget(QListWidget):
    _dependent_on = ['TrackContainer',]
    _fields = ['_index']
    def update(self):
        self.entities = self._Composition.object().tracks.contents
        self.items = [tr.data for tr in self.entities]
        super().update()
    def on_change(self, index):
        super().on_change(index)
        TrackSelector.object().selected = self.entities[self._index]
    def get_repr(self, track_dict):
        return str(track_dict['object'])
    def setup(self):
        super().setup()
        self.setFixedSize(300, 100)

TrackSelector()
