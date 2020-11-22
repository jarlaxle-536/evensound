from .loader import *

from .pointer import *

class Cursor(Entity, CompositionConnected):

    quantization_level = DEFAULT_QUANTIZATION_PARAMETER

    def setup(self):
        self.left_pointer = Pointer()
        self.right_pointer = Pointer()
        super().setup()

    def __str__(self):
        return f'<CURSOR>'

class CursorConnected(Root):
    @property
    def cursor(self):
        if not getattr(self, '_cursor'):
            self._cursor = self.application.state.cursor
        return self._cursor
