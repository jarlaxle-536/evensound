from logic.loader import *

class SomeLabel(QLabel):
    def update(self):
        self.track = self._TrackReprWidget.object().current_track
        self.text = 'lorem ipsum'
        super().update()    

class TrackReprWidget(QWidget):
    _widgets = [
        'SomeLabel',
    ]
    def update(self):
        for obj in self._contents.values():
            obj.update()
    @property
    def current_track(self):
        pass
