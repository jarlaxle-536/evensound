from .loader import *

from .composition import *

@singleton_register('Composition')
class CompositionTitleLabel(QLabelMixin):
    def update(self):
        self.text = self.Composition.title
        super().update()
    def setup(self):
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet('background-color: gray; font-size: 24px;')
        self.setMaximumHeight(100)
        super().setup()
