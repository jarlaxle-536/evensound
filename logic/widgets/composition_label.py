from logic.loader import *

class CompositionLabel(QLabelMixin):
    def update(self):
        self.text = str(self.application.composition.title).upper()
        self.setAlignment(QtCore.Qt.AlignCenter)
