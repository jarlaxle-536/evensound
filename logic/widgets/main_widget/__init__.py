from logic.loader import *

from .composition_title_label import *
from .player_control_panel import *
from .track_list_widget import *
from .track_representation_widget import *
from .alter_button import *
#from .change_title import *

class MainWidget(QWidget):
    _widgets = [
        'CompositionTitleLabel',
        'TrackRepresentationWidget',
        'PlayerControlPanel',
        'TrackListWidget',
        'AlterButton',
    ]
