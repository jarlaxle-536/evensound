from logic.loader import *

class Cursor(Singleton):
    _fields = ['bar_index']
    bar_index = 0
    @property
    def current_bar(self):
        try:
            return self.composition.bars[self.bar_index]
        except Exception:
            return None
    @property
    def composition(self):
        return self._Composition.object()
    def set_bar_index(self, value):
        if self.check_bar_index(value):
            self.bar_index = value
    def check_bar_index(self, value):
        return 0 <= value < length(self.composition.bars)
