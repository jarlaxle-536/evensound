from auxiliary.general import *

class GuiMixin(Root):
    adapted_name = 'gui'
    @classmethod
    def gui_element(cls, inst):
        return getattr(inst, cls.adapted_name)
    def update(self):
        pass

class StateMixin(Root):
    adapted_name = 'state'

class Application(QApplicationMixin, StateMixin):
    pass

class MainWindow(QMainWindowMixin):
    pass
