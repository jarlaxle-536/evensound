from logic.loader import *

class TrackInfoLabel(QLabelMixin):
    text = 'Here will be track info'
    def update(self):
        cursor = Singleton.find('Cursor')
        self.text = f'Cursor points to beat #{cursor.beat_index}.'
        super().update()
