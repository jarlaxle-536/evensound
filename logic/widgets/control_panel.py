from logic.loader import *

class PreviousBeatLayerButton(QPushButtonMixin):
    text = '<<'

class NextBeatLayerButton(QPushButtonMixin):
    text = '>>'

class StopButton(QPushButtonMixin):
    text = 'Stop'

class PlayOrPauseButton(QPushButtonMixin):
    text = 'Play'

class ControlPanel(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    contents = {c.__name__: c for c in [
        StopButton,
        PlayOrPauseButton,
        PreviousBeatLayerButton,
        NextBeatLayerButton
    ]}
