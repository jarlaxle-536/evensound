from .loader import *

class Pointer(Entity):
    beat_index = None
    quantum_index = None
    fields = [
        'beat_index',
        'quantum_index'
    ]
    def setup(self):
        self.check_undefined()
    def check_undefined(self):
#        if any of beat_index or quantum_index is None, make it point to the end
        if any(map(lambda f: getattr(self, f),
            ['beat_index', 'quantum_index'])) is None:
            composition = Singleton.find('Composition')
            self.beat_index = len(composition.beats)
            self.quantum_index = self.beat.quantum_number
    @property
    def composition(self):
        if not getattr(self, '_composition'):
            self._composition = Singleton.find('Composition')
        return self._composition
    @property
    def beat(self):
        return self.composition.beats[self.beat_index - 1]
