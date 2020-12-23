from PyQt5 import QtWidgets, QtCore, QtGui

from .singleton import *

class GuiAdapter(Singleton):
    _gui_constructor = lambda *args, **kwargs: None
    _gui_constructor_args = list()
    _gui_constructor_kwargs = dict()
    def setup(self):
        print(f'{self.__class__.__name__} setup.')
        self.adapt(self._gui_constructor(
                *self._gui_constructor_args,
                **self._gui_constructor_kwargs),
            name='gui'
        )
#        self.initialize_controller()
        super().setup()
#    def initialize_controller(self):
#        controller_cls = self.find(self.controller_cls) or DummyController
#        controller, created = controller_cls.get_or_create()
#        self.adapt(controller, name='controller')
#        self.controller.subscribe_gui(self)
#    @property
#    def data(self):
#        print(f'{self}:data')
#        self._data = self.controller.get_data()
#        return self._data
