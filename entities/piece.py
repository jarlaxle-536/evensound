from .loader import *

from .composition import *

@singleton_register('Composition')
class Piece(Singleton):

    """Memory-only"""

    start, end = 1, None

    fields = [
        'start',
        'end'
    ]

    def setup(self):
        pass
