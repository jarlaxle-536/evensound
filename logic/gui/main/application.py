from logic.loader import *

from logic.entities.state import *

class Application(QApplicationMixin):
    def setup(self):
        self.state = State()
