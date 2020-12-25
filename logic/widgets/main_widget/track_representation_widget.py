from logic.loader import *

class TrackRepresentationWidget(QWidget):
    _widgets = [
        'TrackCanvasLabel',
    ]

class TrackCanvasLabel(QLabel):
    _dependent_on = ['TrackSelector']
    def update(self):
        print(f'{self}:update')
        track = self._TrackSelector.object().selected
        self.text = str(track)
        super().update()
