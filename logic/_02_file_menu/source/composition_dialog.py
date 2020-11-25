from .loader import *

class CompositionTitleRowLabel(FormRowLabelMixin):
    name = 'title'

class CompositionTitleRowInput(QLineEditMixin):
    def setup(self):
        self.entered_text = self.application.state.composition.title
        super().setup()

class CompositionTitleRow(FormRowMixin):
    label_class = CompositionTitleRowLabel
    input_class = CompositionTitleRowInput

class RandomizeCompositionTitleButton(QPushButtonMixin):
    text = 'Randomize title'
    dependent_gui_classes = {
        'CompositionTitleRowInput',
    }
    def setup(self):
        self.faker = faker.Faker()
        super().setup()
    def action(self):
        print('rctb action')
        new_title = self.faker.sentence().replace('.', '')
        self.find('CompositionTitleRow').Input.entered_text = new_title
        print(self.find('CompositionTitleRow').Input.entered_text)
        super().action()
