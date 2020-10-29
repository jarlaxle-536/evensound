from gui.general import *

class MainWidget(WidgetAdapter):
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            Label1,
#            TrackRepr,
            TrackList,
        ]}
        super().setup()

class TrackRepr(WidgetAdapter):
    pass

class TrackList(ListWidgetAdapter):
    def setup(self):
        tracks = self.state.composition.tracks
        self.contents = {
            track.name: f'{track.name}: {track.instrument.code}' 
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
