import logic._01_general_app

from .composition_title_label import *

class MainWidget(logic._01_general_app.MainWidget):
    def setup(self):
        self.contents['CompositionTitleLabel'] = CompositionTitleLabel
        super().setup()
