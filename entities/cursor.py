from .loader import *

class Cursor(Singleton):
    beat_index = 1
    def change_beat_index(self, diff):
        if not getattr(self, 'composition'):
            self.composition = Singleton.find('Composition')
        beat_index_range = [1, len(self.composition.beats)]
        new_index = self.beat_index + diff
        if beat_index_range[0] <= new_index <= beat_index_range[1]:
            self.beat_index = new_index
        else:
            print(f'New cursor index ({new_index}) is out of range: {beat_index_range}')
