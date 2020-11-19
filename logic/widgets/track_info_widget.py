from logic.loader import *

from .track_info_label import *

class TrackInfoWidget(QWidgetMixin):
    contents = {c.__name__: c for c in [
        TrackInfoLabel,
    ]}
