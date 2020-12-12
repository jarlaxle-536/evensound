from logic.loader import *

from .track import *

class Container(Entity):
    _classes = list()
    def setup(self):
        self.contents = list()
        super().setup()
    def insert(self, index, el):
        assert el.__class__ in self._classes
        self.contents = self.contents[:]
        list.insert(self.contents, index, el)

class TrackContainer(Container):
    _classes = [Track, ]
