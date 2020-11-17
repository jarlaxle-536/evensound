from auxiliary import *
from .state import *

class StateMixin(Root):
    def setup(self):
        self.state = State()
