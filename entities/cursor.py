from .loader import *

class Cursor(Singleton):
    beat_index = 1
    track_index = 1
    def change_beat_index(self, diff):
        beat_index_range = [1, len(self.composition.beats)]
        new_index = self.beat_index + diff
        if beat_index_range[0] <= new_index <= beat_index_range[1]:
            self.beat_index = new_index
        else:
            print(f'New cursor index ({new_index}) is out of range: {beat_index_range}')
    def change_track_index(self, val):
        self.track_index = val
    @property
    def composition(self):
        if not getattr(self, '_composition'):
            self._composition = Singleton.find('Composition')
        return self._composition
    @property
    def track(self):
        return self.composition.tracks[self.track_index - 1]
    @property
    def beat(self):
        return self.composition.beats[self.beat_index - 1]
    def __str__(self):
        return f'<CURSOR beat={self.beat_index} track={self.track_index}>'

class CursorConnected(Root):
    @property
    def cursor(self):
        if not getattr(self, '_cursor'):
            self._cursor = self.application.state.cursor
        return self._cursor
