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
    dependent_gui_classes = {
        'InstrumentNameComboBox',
    }
    options = list(Instrument.midi_codes.keys())

class InstrumentTimbreRow(FormRowMixin):
    label_class = InstrumentTimbreLabel
    input_class = InstrumentTimbreComboBox

class InstrumentNameLabel(FormRowLabelMixin):
    name = 'instrument_name'

class InstrumentNameComboBox(QComboBoxMixin):
    def update(self):
        chosen_timbre = GuiMixin.find('InstrumentTimbreComboBox').get_value()
        self.options = list(Instrument.midi_codes[chosen_timbre].values())
        super().update()

class InstrumentNameRow(FormRowMixin):
    label_class = InstrumentNameLabel
    input_class = InstrumentNameComboBox
