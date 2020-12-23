import sys

from .adaptable import *
from .registrable import *
from .updatable import *

class Root(Adaptable, Registrable, Updatable):
    def __str__(self):
        return f'<{self.__class__.__name__}_{self.id}>'
