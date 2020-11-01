from PyQt5.QtWidgets import QApplication

from auxiliary import *

class State:
    pass

class QApplicationAdapter(GuiAdapterMixin):
    constructor = QApplication
    constructor_args = (list(), )

class StateAdapter(StatefulMixin):
    constructor = State

class Application(QApplicationAdapter, StateAdapter):
    pass
