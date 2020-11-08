from entities import *
from gui import *

from .menubar import *
from .control_panel import *

class Application(QApplicationMixin, StateMixin):
    pass

class MainWindow(QMainWindowMixin):
    title = 'EVENSOUND'
#    window_size = (1000, 600)
    menus = [
        FileMenu,
        TrackMenu,
        SettingsMenu
    ]

class SomeLabel(QLabelMixin):
    text = 'lorem ipsum'

class CompositionLabel(QLabelMixin):
    def setup(self):
        self.text = f'Composition: {self.application.composition.title}'
        print(str(self.text))
        super().setup()

class TrackListLabel(QLabelMixin):
    text = 'here will be tracks'

class TrackList(QListWidgetMixin):
    contents = {c.__name__: c for c in [
        TrackListLabel,
    ]}
    def setup(self):
        tracks = self.application.tracks
        self.contents = {str(t): t for t in tracks}
        super().setup()

class CompositionInfo(QWidgetMixin):
    contents = {c.__name__: c for c in [
        CompositionLabel,
    ]}

class TrackInfo(QWidgetMixin):
    contents = {c.__name__: c for c in [

    ]}

class MainWidget(QWidgetMixin):
    contents = {c.__name__: c for c in [
        CompositionInfo,
        TrackList,
        ControlPanel
    ]}
