from PyQt5 import QtWidgets, QtGui, QtCore

from .gui_data import *
from .general import *

class GuiAdapter(Singleton):
    gui_constructor = lambda *args, **kwargs: None
    gui_constructor_args = list()
    gui_constructor_kwargs = dict()
    def setup(self):
        self.adapt(
            self.gui_constructor(
                *self.gui_constructor_args,
                **self.gui_constructor_kwargs
            ), name='gui'
        )
        super().setup()

class QApplication(GuiAdapter):
    gui_constructor = QtWidgets.QApplication
    gui_constructor_args = [list(), ]

class QMainWindow(GuiAdapter):
    gui_constructor = QtWidgets.QMainWindow
    title = 'Main window'
    window_size = MAX_WINDOW_SIZE
    def setup(self):
        super().setup()
        self.show()
    def update(self):
        super().update()
        self.window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip(MAX_WINDOW_SIZE, self.window_size)
        ))
        self.setGeometry(*self.window_centered, *self.window_size)
        self.setWindowTitle(self.title)

class WidgetComposer(Root):
    widgets = list()
    contents = dict()
    def compose(self, target):
        for cls_name in self.widgets:
            obj, created = REGISTER.get(cls_name)[0].get_or_create()
            target.addWidget(obj.gui)
            self.contents = self.contents.copy()
            self.contents[cls_name] = (len(self.contents), obj)

class QWidget(GuiAdapter, WidgetComposer):
    gui_constructor = QtWidgets.QWidget
    layout_type = QtWidgets.QVBoxLayout
    def setup(self):
        super().setup()
        self.layout = self.layout_type.__call__()
        WidgetComposer.compose(self, target=self.layout)
        self.setLayout(self.layout)

class QStackedWidget(GuiAdapter, WidgetComposer):
    gui_constructor = QtWidgets.QStackedWidget
    widgets = list()
    contents = dict()
    def setup(self):
        super().setup()
        WidgetComposer.compose(self, target=self)
    def set_widget(self, cls_name):
        new_index, obj = self.contents.get(cls_name, (0, ) * 2)
        self.setCurrentIndex(new_index)

class QLabel(GuiAdapter):
    gui_constructor = QtWidgets.QLabel
    text = 'Label'
    def update(self):
        super().update()
        self.setText(self.text)

class QPushButton(GuiAdapter):
    gui_constructor = QtWidgets.QPushButton
    text = 'Button'
    def update(self):
        super().update()
        self.setText(self.text)
    def setup(self):
        super().setup()
        self.clicked.connect(self.action)
    def action(self):
        print(f'{self.__class__.__name__} clicked.')
