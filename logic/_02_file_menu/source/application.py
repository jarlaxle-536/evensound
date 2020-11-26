import logic._01_general_app

from .state import *

class Application(logic._01_general_app.Application):
    def setup(self):
        self.state = State()
