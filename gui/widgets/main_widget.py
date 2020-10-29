from gui.general import *
from .control_panel import *

class MainWidget(WidgetAdapter):
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            ControlPanel,
            TrackRepr,
#            TracksList,
        ]}
        super().setup()
#        self.setFixedHeight(300)

class TrackRepr(WidgetAdapter):
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            Label1,
        ]}
        super().setup()

class TracksList(ListWidgetAdapter):
    def setup(self):
        tracks = self.state.composition.tracks
        self.contents = {
            track.name: f'{track.name}: {track.instrument.name_expanded}'
            for track in tracks
        }
        super().setup()

class Label1(LabelAdapter):
    def setup(self):
        self.text = f'composition dict: {self.state.composition.__dict__}'
        for t in self.state.composition.tracks:
            print(t.__dict__)
        for b in self.state.composition.beats:
            print(b.__dict__)
        super().setup()
