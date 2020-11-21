from logic.loader import *

from logic.functions import *

class PreviousBeatLayerButton(QPushButtonMixin, CursorConnected):
    dependent_gui_classes = {
        'TrackInfoLabel'
    }
    text = '<<'
    def action(self):
        self.cursor.change_beat_index(-1)
        super().action()

class NextBeatLayerButton(QPushButtonMixin, CursorConnected):
    dependent_gui_classes = {
        'TrackInfoLabel'
    }
    text = '>>'
    def action(self):
        self.cursor.change_beat_index(1)
        super().action()

class StopButton(QPushButtonMixin):
    text = 'Stop'

class PlayOrPauseButton(QPushButtonMixin):
    text = 'Play'

class AlternateButton(QPushButtonMixin, CursorConnected):
    dependent_gui_classes = {
        'TrackInfoLabel'
    }
    text = 'Alternate'
    def action(self):
        print(f'cursor: {self.cursor}')
        alternate(self.cursor.track, self.cursor.beat)
        super().action()

class ControlPanel(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    contents = {c.__name__: c for c in [
        StopButton,
        PlayOrPauseButton,
        PreviousBeatLayerButton,
        NextBeatLayerButton,
        AlternateButton
    ]}
