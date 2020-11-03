from auxiliary import *
from .state import *

class StateMixin(Root):
    def __init__(self, **kwargs):
        self.state = State()
        super().__init__(**kwargs)
