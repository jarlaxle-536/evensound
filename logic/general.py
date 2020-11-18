from entities import *
from gui import *

from .menubar import *
from .control_panel import *

class LogicMixin(Root):
    pass

class EntifiedGui(GuiMixin):
    entity = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if isinstance(self.entity, Entity):
            self.entity.connected_guis = getatttr(self.entity,
                'connected_guis', list()).copy() + [self, ]

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

class CompositionLabel(QLabelMixin):
    def setup(self):
        self.text = str(self.application.composition.title).upper()
        self.setAlignment(QtCore.Qt.AlignCenter)
        super().setup()

class TrackList(QListWidgetMixin):
    def setup(self):
        tracks = self.application.state.composition.tracks
        self.contents = {str(t): t for t in tracks}
        super().setup()

class CompositionInfo(QWidgetMixin):
    contents = {c.__name__: c for c in [
        CompositionLabel,
    ]}

class TrackInfoLabel(QLabelMixin):
    text = 'Here will be track info'

class TrackInfo(QWidgetMixin):
    contents = {c.__name__: c for c in [
        TrackInfoLabel,
    ]}

class MainWidget(QWidgetMixin):
    contents = {c.__name__: c for c in [
        CompositionInfo,
        TrackInfo,
        TrackList,
        ControlPanel
    ]}
