from logic.loader import *

from .track import *

class TrackContainer(Entity):
    def insert(self, i, elem):
        assert isinstance(elem, Track)
        return list.insert(self.contents, i, elem)
    def setup(self):
        self.contents = list()
        super().setup()
        self.insert(0, Track())
        self.insert(1, Track())
