from logic.loader import *

from .composition_title_label import *
from .player_control_panel import *
#from .change_title import *
#from .track_repr_widget import *
#from .track_selector_widget import *

class MainWidget(QWidget):
    _widgets = [
        'CompositionTitleLabel',
        'PlayerControlPanel',
    ]
