import faker
import sys

from entities import *
from .general import *

class CompositionTitleLabel(FormRowLabelMixin):
    name = 'title'

class CompositionTitleInput(QLineEditMixin):
    pass

class CompositionTitleRow(FormRowMixin):
    label_class = CompositionTitleLabel
    input_class = CompositionTitleInput

class RandomizeCompositionTitleButton(QPushButtonMixin):
    text = 'Randomize title'
    def setup(self):
        super().setup()
        self.faker = faker.Faker()
        self.connect_to_func(self.action)
    def action(self):
        title = self.faker.sentence().replace('.', '')
        title_input = self.find('CompositionTitleRow').Input
        title_input.entered_text = title
        title_input.setup()

class NewCompositionCancelButton(QPushButtonMixin):
    text = 'Cancel'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        dialog = self.find('NewCompositionDialog')
        dialog.close()

class NewCompositionOKButton(QPushButtonMixin):
    text = 'OK'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        data = self.find('NewCompositionWidget').acquire()
        composition = Composition(**data)
        print(composition.__dict__)
        self.application.state.set_composition(composition)
        dialog = self.find('NewCompositionDialog')
        dialog.close()
        self.find('CompositionLabel').setup()
    def refine_data(self, data):
        return data

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
