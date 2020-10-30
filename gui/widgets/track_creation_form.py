from entities.instrument import *
from gui.general import *

class TrackCreationForm(DialogAdapter):
    title = 'Adding track'
    window_size = (600, 300)
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            TrackNameLE,
            SelectInstrumentCB,
            CreateTrackButton,
        ]}
        super().setup()

class TrackNameLE(LineEditWithCaption):
    text = 'Track name:'

class SelectInstrumentCB(ComboBoxWithCaption):
    text = 'Instrument:'
    options = Instrument.choices

class CreateTrackButton(ButtonAdapter):
    title = 'Create track'
    def action(self):
        dialog_adapter = self.parent().adapter
        print('track name:', dialog_adapter.contents['TrackNameLE'].entered_text)
        print('track instrument:', dialog_adapter.contents['SelectInstrumentCB'].selected)
