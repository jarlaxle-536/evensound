from logic.loader import *

class TrackListWidget(QListWidgetMixin):
    dependent_gui_classes = [
        'TrackInfoLabel'
    ]

    def setup(self):
        self.track_selector = self.application.state.track_selector
        super().setup()

    def update(self):
        tracks = self.application.state.composition.tracks
        print('TRACKS:', self.application.state.composition.tracks)
        self.contents = {str(t): t for t in tracks}
        super().update()

    def index_changed(self, index):
        self.track_selector.change_index(index + 1)
        super().action()
