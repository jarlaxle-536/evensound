from .loader import *

from .composition import *

class Piece(Singleton):

    """Memory-only"""

    composition = None
    start, end = 1, None

    fields = [
        'composition',
        'start',
        'end'
    ]

    def setup(self):
        pass
