from logic.loader import *

class TrackListWidget(QListWidgetMixin):
    def update(self):
        tracks = self.application.state.composition.tracks
        print('TRACKS:', self.application.state.composition.tracks)
        self.contents = {str(t): t for t in tracks}
        super().update()
