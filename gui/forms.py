from .general import *

"""
    Both QLineEditMixin and QComboBoxMixin are declared here,
    since they are assumed to be used in forms only.
"""

class QLineEditMixin(GuiMixin):
    constructor = QtWidgets.QLineEdit
    entered_text = ''
    def setup(self):
        super().setup()
        self.setText(self.entered_text)
        self.textChanged[str].connect(self.on_change)
    def get_value(self):
        print(f'{self.__class__.__name__} entered text: {self.entered_text}')
        return self.entered_text
    def on_change(self, text):
        print(f'{self.__class__.__name__} has changed: {text}')
        self.entered_text = text

class QComboBoxMixin(GuiMixin):
    constructor = QtWidgets.QComboBox
    options = list()
    def setup(self):
        super().setup()
        self.clear()
        for opt in self.options:
            self.addItem(opt)
        self.currentIndexChanged.connect(self.on_change)
    def get_value(self):
        return self.options[self.currentIndex()]
    def on_change(self, new_index):
        print(f'{self.__class__.__name__} has changed: {new_index}')

class FormRowLabelMixin(QLabelMixin):
    name = 'name'
    def setup(self):
        self.text = f'{entity_field_hr(self.name)}:'
        super().setup()

class FormRowMixin(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    def setup(self):
        self.contents = {
            'Label': self.label_class,
            'Input': self.input_class
        }
        super().setup()
    def acquire(self):
        return (self.Label.name, self.Input.get_value())

class FormDataMixin(Root):
    form_fields = list()
    def acquire(self):
        rows = [cls.find(cls.__name__) for t, cls in self.contents.items()
            if t in self.form_fields]
        data = dict([row.acquire() for row in rows])
        return self.refine_data(data)
    def refine_data(self, data):
        return data
