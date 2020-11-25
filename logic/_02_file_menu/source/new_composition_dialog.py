from .composition_dialog import *

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
        self.application.state.set_composition(composition)
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
