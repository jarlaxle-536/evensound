from logic.loader import *

class SomeLabel(QLabel):
    def update(self):
        self.bar = self._State.object().cursor.current_bar
        self.text = str(self._TrackSelectorWidget.object().selected) + ', '
        self.text += str(self.bar)
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
