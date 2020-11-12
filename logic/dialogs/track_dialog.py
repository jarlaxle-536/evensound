from entities import *
from .general import *

class TrackNameRow(FormRowMixin):
    name = 'name'

class InstrumentTimbreComboBox(QComboBoxMixin):
    options = Instrument.instrument_timbre_choices

class InstrumentComboBox(QComboBoxMixin):
    options = Instrument.instrument_code_choices

class InstrumentTimbreRow(FormRowMixin):
    name = 'instrument_timbre'
    input_type = InstrumentTimbreComboBox

class InstrumentRow(FormRowMixin):
    name = 'instrument'
    input_type = InstrumentComboBox

class AddTrackCancelButton(QPushButtonMixin):
    text = 'Cancel'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        dialog = self.find('AddTrackDialog')
        dialog.close()

class AddTrackOKButton(QPushButtonMixin):
    text = 'OK'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        dialog = self.find('AddTrackDialog')
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
        TrackNameRow,
        InstrumentTimbreRow,
        InstrumentRow,
        AddTrackControlPanel,
    ]}

class AddTrackDialog(QDialogMixin):
    title = 'Add track'
    central_widget = AddTrackWidget
