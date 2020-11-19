from .composition_dialog import *

class EditCompositionCancelButton(QPushButtonMixin):
    text = 'Cancel'
    def action(self):
        dialog = self.find('EditCompositionDialog')
        dialog.close()
        super().action()

class EditCompositionOKButton(QPushButtonMixin):
    text = 'OK'
    dependent_gui_classes = {
        'CompositionLabel',
    }
    def action(self):
        data = self.find('EditCompositionWidget').acquire()
        self.application.state.composition.__dict__.update(data)
        dialog = self.find('EditCompositionDialog')
        dialog.close()
        super().action()

class EditCompositionControlPanel(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    contents = {cls.__name__: cls for cls in [
        EditCompositionCancelButton,
        EditCompositionOKButton
    ]}

class EditCompositionWidget(QWidgetMixin, FormDataMixin):
    form_fields = ['CompositionTitleRow']
    contents = {cls.__name__: cls for cls in [
        CompositionTitleRow,
        RandomizeCompositionTitleButton,
        EditCompositionControlPanel,
    ]}
    def refine_data(self, data):
        res = dict()
        res['title'] = data['title']
        return res

class EditCompositionDialog(QDialogMixin):
    title = 'Edit composition'
    central_widget = EditCompositionWidget
