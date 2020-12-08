from logic.loader import *

from .play_or_stop_button import *

class SomeLabel(QLabel):
    pass

class MainWidget(QWidget):
    _widgets = [
        'SomeLabel',
        'PlayOrStopButton'
    ]
