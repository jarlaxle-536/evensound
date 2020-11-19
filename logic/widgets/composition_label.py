from logic.loader import *

class CompositionLabel(QLabelMixin):
    def update(self):
        self.text = str(self.application.composition.title).upper()
        print(self.text)
        self.setAlignment(QtCore.Qt.AlignCenter)
        super().update()
