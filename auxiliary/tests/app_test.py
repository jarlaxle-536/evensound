from auxiliary.mixins import *

class SomeGui:
    pass

class SomeState:
    pass

class ApplicationAdapter(GuiAdapterMixin):
    constructor = SomeGui

class StateAdapter(StatefulMixin):
    constructor = SomeState

class Application(ApplicationAdapter, StateAdapter):
    pass

app = Application()
print(app.__dict__)
