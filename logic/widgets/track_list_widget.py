from logic.loader import *

class TrackListWidget(QListWidgetMixin, CursorConnected):
    dependent_gui_classes = [
        'TrackInfoLabel'
    ]
    def update(self):
        tracks = self.application.state.composition.tracks
        print('TRACKS:', self.application.state.composition.tracks)
        self.contents = {str(t): t for t in tracks}
        super().update()

    def index_changed(self, index):
        self.cursor.change_track_index(index + 1)
        super().action()
