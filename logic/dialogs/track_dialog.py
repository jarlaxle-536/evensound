from logic.loader import *

class TrackNameLabel(FormRowLabelMixin):
    name = 'name'

class TrackNameInput(QLineEditMixin):
    pass

class TrackNameRow(FormRowMixin):
    label_class = TrackNameLabel
    input_class = TrackNameInput

class InstrumentTimbreLabel(FormRowLabelMixin):
    name = 'instrument_timbre'

class InstrumentTimbreComboBox(QComboBoxMixin):
    options = list(Instrument.midi_codes.keys())
    def on_change(self):
        GuiMixin.find('InstrumentNameComboBox').setup()

class InstrumentTimbreRow(FormRowMixin):
    label_class = InstrumentTimbreLabel
    input_class = InstrumentTimbreComboBox

class InstrumentNameLabel(FormRowLabelMixin):
    name = 'instrument_name'

class InstrumentNameComboBox(QComboBoxMixin):
    def setup(self):
        chosen_timbre = GuiMixin.find('InstrumentTimbreComboBox').get_value()
        self.options = list(Instrument.midi_codes[chosen_timbre].values())
        super().setup()

class InstrumentNameRow(FormRowMixin):
    label_class = InstrumentNameLabel
    input_class = InstrumentNameComboBox

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
    def refine_data(self, data):
        return data

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
