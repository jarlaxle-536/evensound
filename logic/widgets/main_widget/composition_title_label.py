from logic.loader import *

from logic.entities import *

class CompositionTitleLabel(QLabel):
    _dependent_on = ['Composition']
    def update(self):
        self.text = Composition.object().title
        super().update()
    def setup(self):
        super().setup()
        self.setFont(QtGui.QFont('Times', 20))
        self.setAlignment(QtCore.Qt.AlignCenter)
