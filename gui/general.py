from PyQt5 import QtCore, QtGui, QtWidgets

class GuiAdapter:

    adapted_name = 'gui'
    gui_args = tuple()
    gui_kwargs = dict()

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.set_gui()
        self.setup()

    def set_gui(self):
        self.gui = self.gui_constructor(*self.gui_args, **self.gui_kwargs)
        self.gui.adapter = self
        return self.gui

    def setup(self):
        pass

    def update(self):
        pass

    def find_by_class(self, cls_name):
        obj = self
        while not obj is None:
            print(obj)
            if obj.__class__.__name__ == cls_name:
                return obj
            obj = obj.parent().adapter

    def __getattr__(self, attr_name):
        return getattr(self.gui, attr_name)

    @property
    def application(self):
        return QtWidgets.QApplication.instance().adapter

class ApplicationAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QApplication
    gui_args = ([], )
    state = None

    def print_debug_info(self):
        print('=' * 50)
        print('DEBUG INFO')
        print(f'state: {self.state}')
        print('=' * 50)

class MainWindowAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QMainWindow
    window_size = (1400, 800)
    window_centered = tuple(map(
        lambda t: (t[0] - t[1]) // 2, zip((1400, 800), window_size)
    ))
    def setup(self):
        self.setWindowTitle(self.title)
        self.setGeometry(*self.window_centered, *self.window_size)
        self.show()
        super().setup()

class WidgetAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QWidget
    layout_type = QtWidgets.QVBoxLayout
    def setup(self):
        layout = self.layout_type()
        for component in self.contents.values():
            layout.addWidget(component.gui)
        self.setLayout(layout)
        super().setup()

class StackedWidgetAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QStackedWidget
    def setup(self):
        for widget in self.contents.values():
            self.gui.addWidget(widget.gui)
        super().setup()
    def change_widget(self, widget_name):
        widget_index = list(self.contents).index(widget_name) \
            if widget_name in self.contents else None
        if not widget_index is None:
            self.setCurrentIndex(widget_index)

class ButtonAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QPushButton
    title = 'Button'
    def set_gui(self):
        self.gui_args = (self.title, )
        super().set_gui()
    def setup(self):
        self.gui.clicked.connect(self.action)
        super().setup()
    def action(self):
        print(f'Doing action for {self.__class__.__name__}')
        self.application.print_debug_info()

class LabelAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QLabel
    text = 'Label'
    def set_gui(self):
        self.gui_args = (self.text, )
        super().set_gui()
    def setup(self):
        self.setText(self.text)

class ActionAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QAction
    text = 'Action'
    shortcut = 'Enter'
    tip = 'Action tip'
    def setup(self):
        self.setText(self.text)
        self.setShortcut(self.shortcut)
        self.setStatusTip(self.tip)
        self.gui.triggered.connect(self.action)
        super().setup()
    def action(self):
        print(f'Doing action for {self.__class__.__name__}')
