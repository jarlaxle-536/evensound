from logic.loader import *

class Cursor(Singleton):
    bar_index = 1
    @property
    def current_bar(self):
        return self._Composition.object().bars[self.bar_index - 1]
