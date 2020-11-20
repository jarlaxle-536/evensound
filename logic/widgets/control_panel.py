from logic.loader import *

class PreviousBeatLayerButton(QPushButtonMixin):
    dependent_gui_classes = {
        'TrackInfoLabel'
    }
    text = '<<'
    def setup(self):
        super().setup()
        self.cursor = Singleton.find('Cursor')
    def action(self):
        self.cursor.change_beat_index(-1)
        super().action()

class NextBeatLayerButton(QPushButtonMixin):
    dependent_gui_classes = {
        'TrackInfoLabel'
    }
    text = '>>'
    def setup(self):
        super().setup()
        self.cursor = Singleton.find('Cursor')
    def action(self):
        self.cursor.change_beat_index(1)
        super().action()

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
