from logic.loader import *

class Container(Entity):
    _classes = list()
    def setup(self):
        self.contents = list()
        super().setup()
    def insert(self, index, el):
        assert el.__class__ in self._classes
        self.contents = self.contents[:]
        list.insert(self.contents, index, el)
    def __len__(self):
        return len(self.contents)
    def __getitem__(self, index):
        return self.contents[index]
