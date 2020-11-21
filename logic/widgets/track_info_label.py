from logic.loader import *

class TrackInfoLabel(QLabelMixin, CursorConnected):
    text = 'Here will be track info'
    def update(self):
        print(self.application.composition.sounds)
        sounds = []
        for b in self.application.composition.beats:
            sounds += b.sounds
        lines = [
            f'Cursor: {self.cursor}',
            f'Present sounds: {" ".join(map(str, sounds))}'
        ]
        self.text = '\n'.join(lines)
        super().update()
