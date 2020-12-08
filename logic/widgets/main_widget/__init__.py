from logic.loader import *

from .play_or_stop_button import *
from .change_title import *
from .composition_title_label import *

class MainWidget(QWidget):
    _widgets = [
        'CompositionTitleLabel',
        'ChangeTitleButton',
        'PlayOrStopButton'
    ]
