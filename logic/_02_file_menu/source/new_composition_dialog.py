from .loader import *

from .composition import *

class CompositionTitleRowLabel(FormRowLabelMixin):
    name = 'title'

@singleton_register('Composition')
class CompositionTitleRowInput(QLineEditMixin):
    def update(self):
        self.entered_text = self.Composition.title
        super().update()

class CompositionTitleRow(FormRowMixin):
    label_class = CompositionTitleRowLabel
    input_class = CompositionTitleRowInput

@singleton_register('Composition')
class RandomizeCompositionTitleButton(QPushButtonMixin):
    text = 'Randomize title'
    def setup(self):
        self.faker = faker.Faker()
        super().setup()
    def action(self):
        new_title = self.faker.sentence().replace('.', '')
        self.Composition.title = new_title

class NewCompositionCancelButton(QPushButtonMixin):
    text = 'Cancel'
    def action(self):
        dialog = self.find('NewCompositionDialog')
        dialog.close()
        super().action()

class NewCompositionOKButton(QPushButtonMixin):
    text = 'OK'
    def action(self):
        data = self.find('NewCompositionWidget').acquire()
        composition = Composition(**data)
        print(composition.__dict__)
        self.application.state.composition = composition
        dialog = self.find('NewCompositionDialog')
        dialog.close()
        super().action()

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
    def refine_data(self, data):
        res = data.copy()
        return res

class NewCompositionDialog(QDialogMixin):
    title = 'New composition'
    central_widget = NewCompositionWidget
