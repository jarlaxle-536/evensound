import logic._02_file_menu

from .state import *

class Application(logic._02_file_menu.Application):
    def setup(self):
        self.state = State()
