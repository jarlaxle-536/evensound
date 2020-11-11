import faker
import sys

from .general import *

class CompositionTitleRow(FormRowMixin):
    name = 'title'

class RandomizeCompositionTitleButton(QPushButtonMixin):
    text = 'Randomize title'
    def setup(self):
        super().setup()
        self.faker = faker.Faker()
        self.connect_to_func(self.action)
    def action(self):
        title = self.faker.sentence()
        print(title)

class NewCompositionCancelButton(QPushButtonMixin):
    text = 'Cancel'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        print('new cmp cancel')

class NewCompositionOKButton(QPushButtonMixin):
    text = 'OK'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        data = self.find_by_classname('NewCompositionWidget').acquire()
        print(data)

class NewCompositionControlPanel(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    contents = {cls.__name__: cls for cls in [
        NewCompositionCancelButton,
        NewCompositionOKButton
    ]}

class NewCompositionWidget(QWidgetMixin, FormDataMixin):
    form_fields = ['CompositionTitleRow']
    contents = {cls.__name__: cls for cls in [
        CompositionTitleRow,
        RandomizeCompositionTitleButton,
        NewCompositionControlPanel,
    ]}

class NewCompositionDialog(QDialogMixin):
    title = 'New composition'
    central_widget = NewCompositionWidget
