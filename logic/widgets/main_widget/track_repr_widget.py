from logic.loader import *

class SomeLabel(QLabel):
    def update(self):
        self.text = self._TrackSelectorWidget.object().selected.name
        super().update()

class TrackReprWidget(QWidget):
    _widgets = [
        'SomeLabel',
    ]
    _subscriptions = {
        ('TrackSelectorWidget', 'selected'),
    }
    def update(self):
        for index, obj in self._contents.values():
            obj.update()
