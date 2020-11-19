from logic.general import *

class CompositionLabel(QLabelMixin):
    def setup(self):
        self.text = str(self.application.composition.title).upper()
        self.setAlignment(QtCore.Qt.AlignCenter)
        super().setup()
