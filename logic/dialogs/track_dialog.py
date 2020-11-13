from entities import *
from .general import *

class TrackNameRow(FormRowMixin):
    name = 'name'

class InstrumentTimbreComboBox(QComboBoxMixin):
    options = list(Instrument.midi_codes.keys())
    def on_change(self):
        GuiMixin.find('InstrumentNameComboBox').setup()

class InstrumentNameComboBox(QComboBoxMixin):
    def setup(self):
        chosen_timbre = GuiMixin.find('InstrumentTimbreComboBox').get_value()
        self.options = list(Instrument.midi_codes[chosen_timbre].values())
        super().setup()

class InstrumentTimbreRow(FormRowMixin):
    name = 'instrument_timbre'
    input_type = InstrumentTimbreComboBox

class InstrumentNameRow(FormRowMixin):
    name = 'instrument_name'
    input_type = InstrumentNameComboBox

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
        data = self.find('NewTrackWidget').acquire()
        composition = self.application.state.composition
        print(f'Acquired data: {data}')
#        composition.add_track(**data)
        dialog = self.find('NewTrackDialog')
        dialog.close()

class NewTrackControlPanel(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    contents = {cls.__name__: cls for cls in [
        NewTrackCancelButton,
        NewTrackOKButton
    ]}

class NewTrackWidget(QWidgetMixin, FormDataMixin):
    form_fields = ['TrackNameRow', 'InstrumentTimbreRow', 'InstrumentNameRow']
    contents = {cls.__name__: cls for cls in [
        TrackNameRow,
        InstrumentTimbreRow,
        InstrumentNameRow,
        NewTrackControlPanel,
    ]}

class NewTrackDialog(QDialogMixin):
    title = 'New track'
    central_widget = NewTrackWidget
