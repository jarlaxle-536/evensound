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

class PlayOrPauseButton(QPushButtonMixin, CursorConnected):
    text = 'Play'
    def action(self):
        composition = self.application.state.composition
        midi = composition.create_midi()
        current_output = self.application.state.player.midi_output
#        play_on_midi_output(current_output)
        track = self.cursor.track
#        current_output.set_instrument(31)
        for s in track.sounds:
            if not s.pitch is None:
                current_output.note_on(s.pitch, 127)
                time.sleep(0.2)
                current_output.note_off(s.pitch, 127)
            else:
                time.sleep(0.2)

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
        PlayOrPauseButton,
        PreviousBeatLayerButton,
        NextBeatLayerButton,
        AlternateButton
    ]}
