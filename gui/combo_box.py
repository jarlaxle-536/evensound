from auxiliary import *

from .label import *
from .widget import *

class QComboBox(GuiAdapter):
    _gui_constructor = QtWidgets.QComboBox
    options = list()
    selected = None
    def setup(self):
        super().setup()
        self.indexed_options = {
            i: dict(zip(['str', 'object'], self.options[i]))
            for i in range(len(self.options))
        }
        for opt_str, obj in self.options:
            self.addItem(opt_str)
        self.on_change(0)
        self.currentIndexChanged.connect(self.on_change)
    def on_change(self, index):
        print(f'{self} on_change with {index}')
        self.selected = self.indexed_options[index]['object']
        print(f'{self} selected: {self.selected}')
        print(f'{self} adapter: {self.adapter}')
        try:
            self.adapter.set_selected(self.selected)
        except Exception:
            pass

class QComboBoxWithLabel(QWidget):
    _layout_type = QtWidgets.QHBoxLayout
    _text = 'Combo box w/label'
    _options = list()
    def setup(self):
        super().setup()
        self.adapt(QLabel(text=self._text), name='label')
        self.adapt(QComboBox(options=self._options), name='combo_box')
        self._layout.addWidget(self.label.gui)
        self._layout.addWidget(self.combo_box.gui)
    def set_selected(self, obj):
        self.selected = obj
