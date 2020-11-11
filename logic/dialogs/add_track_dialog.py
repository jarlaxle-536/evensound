from .general import *

class AddTrackCancelButton(QPushButtonMixin):
    text = 'Cancel'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        dialog = self.find_by_classname('AddTrackDialog')
        dialog.close()

class AddTrackOKButton(QPushButtonMixin):
    text = 'OK'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
#        data = self.find_by_classname('AddTrackWidget').acquire()
#        print(data)
#        'do smth with acquired data'
        dialog = self.find_by_classname('AddTrackDialog')
        dialog.close()

class AddTrackControlPanel(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    contents = {cls.__name__: cls for cls in [
        AddTrackCancelButton,
        AddTrackOKButton
    ]}

class AddTrackWidget(QWidgetMixin, FormDataMixin):
    form_fields = []
    contents = {cls.__name__: cls for cls in [
        AddTrackControlPanel,
    ]}

class AddTrackDialog(QDialogMixin):
    title = 'Add track'
    central_widget = AddTrackWidget
