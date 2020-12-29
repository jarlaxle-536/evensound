from logic.loader import *

class Container(Entity):
    _cls = None
    def setup(self):
        self.contents = list()
        super().setup()
    def insert(self, el, index=None):
        assert el.__class__ == self._cls
        index = index if index is not None else len(self.contents)
        self.contents = self.contents[:]
        list.insert(self.contents, index, el)
    def __len__(self):
        return len(self.contents)
    def __getitem__(self, index):
        return self.contents[index]
