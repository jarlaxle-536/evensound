from logic.loader import *

class CompositionTitleLabel(QLabel):
    _subscriptions = {
        ('Composition', 'title'),
    }
    def update(self):
        self.text = self._Composition.object().title
        super().update()
    def setup(self):
        super().setup()
        self.setFont(QtGui.QFont('Times', 20))
