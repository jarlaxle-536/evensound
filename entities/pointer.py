from .loader import *

class Pointer(Entity, CompositionConnected):
    _beat_index = None
    _quantum_index = None
    fields = [
        '_beat_index',
        '_quantum_index'
    ]
    @property
    def beat_index(self):
        if getattr(self, '_beat_index') is None:
            self._beat_index = len(self.composition.beats)
        return self._beat_index
    @property
    def quantum_index(self):
        if getattr(self, '_quantum_index') is None:
            self._quantum_index = self.composition.beats[-1].quantum_number
        return self._quantum_index
    @property
    def beat(self):
        return self.composition.beats[self.beat_index - 1]
