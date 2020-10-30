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

    @property
    def state(self):
        return self.application.state

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

class ListWidgetAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QListWidget
    def setup(self):
        for component in self.contents.values():
            self.addItem(component)
        super().setup()

class DialogAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QDialog
    layout_type = QtWidgets.QVBoxLayout
    window_size = (600, 400)
    def setup(self):
        self.layout = self.layout_type()
        for widget in self.contents.values():
            self.layout.addWidget(widget.gui)
        self.setLayout(self.layout)
        self.setWindowTitle(self.title)
        window_centered = tuple(map(
            lambda t: (t[0] - t[1]) // 2, zip((1400, 800), self.window_size)
        ))
        self.setGeometry(*window_centered, *self.window_size)
        self.show()
        super().setup()

class LineEditWithCaption(WidgetAdapter):
    layout_type = QtWidgets.QHBoxLayout
    text = 'Line edit text'
    def setup(self):
        self.contents = {
            'Label': LabelAdapter(text=self.text),
            'LineEdit': LineEditAdapter()
        }
        super().setup()
    @property
    def entered_text(self):
        return self.contents['LineEdit'].text()

class LineEditAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QLineEdit

class ComboBoxWithCaption(WidgetAdapter):
    layout_type = QtWidgets.QHBoxLayout
    text = 'Combo box text'
    options = list()
    def setup(self):
        self.contents = {
            'Label': LabelAdapter(text=self.text),
            'ComboBox': ComboBoxAdapter(options=self.options)
        }
        super().setup()
    @property
    def selected(self):
        return self.contents['ComboBox'].selected

class ComboBoxAdapter(GuiAdapter):
    gui_constructor = QtWidgets.QComboBox
    choice_mapping = dict()
    options = list()
    selected = None
    def setup(self):
        for value, repr in self.options:
            self.choice_mapping[repr] = value
            self.addItem(repr)
        self.activated[str].connect(self.on_selection)
    def on_selection(self, repr):
        print(repr)
        self.selected = self.choice_mapping[repr]
        print(self.selected)

class GeneralThread(QtCore.QThread):
    waiting = alive = True
    period = 1
    def __init__(self, **kwargs):
        super().__init__()
        self.finish = QtCore.pyqtSignal()
    def run(self):
        while self.alive:
            if not self.waiting:
                self.adapter.action()
            QtCore.QThread.msleep(1000 * self.period)
        self.finish.emit()
    def __del__(self):
        self.terminate()
        self.quit()
    def stop_thread(self):
        self.alive = False
    def toggle_activity(self):
        print(f'Toggling activity for {self.__class__.__name__}')
        self.waiting = not self.waiting

class ThreadAdapter(GuiAdapter):
    gui_constructor = GeneralThread
    def setup(self):
        super().setup()
        self.gui.start()
    def action(self):
        raise ValueError('Thread action should be defined in subclass.')
