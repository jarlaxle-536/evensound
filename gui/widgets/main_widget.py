from gui.general import *

class MainWidget(WidgetAdapter):
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            TrackRepr,
            TrackList,
        ]}
        super().setup()

class TrackRepr(WidgetAdapter):
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            Label1,
            ControlPanel,
        ]}
        super().setup()

class TrackList(ListWidgetAdapter):
    def setup(self):
        tracks = self.state.composition.tracks
        self.contents = {
            track.name: f'{track.name}: {track.instrument.name_expanded}'
            for track in tracks
        }
        super().setup()

class ControlPanel(WidgetAdapter):
    layout_type = QtWidgets.QHBoxLayout
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            PlayOrStopButton,
        ]}
        super().setup()

class PlayOrStopButton(ButtonAdapter):
    title = 'Play'
    def setup(self):
        super().setup()
        self.play_thread = PlayThread()
    def update(self):
        self.title = {True: 'Play', False: 'Stop'}.get(
            self.play_thread.waiting, 'ERROR')
        self.setText(self.title)
    def action(self):
        print('playing or stopping')
        self.play_thread.toggle_activity()
        self.update()

class PlayThread(ThreadAdapter):
    def action(self):
        print('PLAY THREAD')

class Label1(LabelAdapter):
    def setup(self):
        self.text = f'composition dict: {self.state.composition.__dict__}'
        for t in self.state.composition.tracks:
            print(t.__dict__)
        for b in self.state.composition.beats:
            print(b.__dict__)
        super().setup()
