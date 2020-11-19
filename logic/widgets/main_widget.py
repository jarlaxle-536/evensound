from logic.loader import *

from .composition_info_widget import *
from .track_info_widget import *
from .track_list_widget import *
from .control_panel import *

class MainWidget(QWidgetMixin):
    contents = {c.__name__: c for c in [
        CompositionInfoWidget,
        TrackInfoWidget,
        TrackListWidget,
        ControlPanel
    ]}
