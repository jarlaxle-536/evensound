from logic.loader import *

class TrackSelector(Singleton):
    _dependent_on = ['TrackListWidget']
    _fields = ['selected']
    def update(self):
        track_list_widget = TrackListWidget.object()
        try:
            self.selected = track_list_widget.entities[track_list_widget._index]
        except: pass

class TrackListWidget(QListWidget):
    _dependent_on = ['TrackContainer',]
    _fields = ['_index']
    def update(self):
        self.entities = self._Composition.object().tracks.contents
        self.items = [tr.data for tr in self.entities]
        super().update()
    def get_repr(self, track_dict):
        return str(track_dict['object'])
    def setup(self):
        super().setup()
        self.setFixedSize(300, 100)

TrackSelector()
