from entities import *
from .general import *

class TrackNameRow(FormRowMixin):
    name = 'name'

class InstrumentTimbreComboBox(QComboBoxMixin):
    options = Instrument.instrument_timbre_choices
    def on_change(self):
        GuiMixin.find('InstrumentComboBox').setup()

class InstrumentComboBox(QComboBoxMixin):
    options = Instrument.instrument_code_choices
    def setup(self):
        instrument_timbre = GuiMixin.find('InstrumentTimbreComboBox').get_value()
        self.options = MIDI_CODES[instrument_timbre].values()
        super().setup()

class InstrumentTimbreRow(FormRowMixin):
    name = 'instrument_timbre'
    input_type = InstrumentTimbreComboBox

class InstrumentRow(FormRowMixin):
    name = 'instrument'
    input_type = InstrumentComboBox

class NewTrackCancelButton(QPushButtonMixin):
    text = 'Cancel'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        dialog = self.find('NewTrackDialog')
        dialog.close()

class NewTrackOKButton(QPushButtonMixin):
    text = 'OK'
    def setup(self):
        super().setup()
        self.connect_to_func(self.action)
    def action(self):
        dialog = self.find('NewTrackDialog')
        dialog.close()

class NewTrackControlPanel(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    contents = {cls.__name__: cls for cls in [
        NewTrackCancelButton,
        NewTrackOKButton
    ]}

class NewTrackWidget(QWidgetMixin, FormDataMixin):
    form_fields = []
    contents = {cls.__name__: cls for cls in [
        TrackNameRow,
        InstrumentTimbreRow,
        InstrumentRow,
        NewTrackControlPanel,
    ]}

class NewTrackDialog(QDialogMixin):
    title = 'New track'
    central_widget = NewTrackWidget
