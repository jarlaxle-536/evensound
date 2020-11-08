from entities import *
from gui import *

from logic.menubar import *

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

class Button1(QPushButtonMixin):
    text = 'Button1'

class Button2(QPushButtonMixin):
    text = 'Button2'

class Button3(QPushButtonMixin):
    text = 'Button3'

class CompositionLabel(QLabelMixin):
    def setup(self):
        self.text = self.application.composition.title
        print(str(self.text))
        super().setup()

class TrackListLabel(QLabelMixin):
    text = 'here will be tracks'

class TrackList(QWidgetMixin):
    contents = {c.__name__: c for c in [
        TrackListLabel,
    ]}

class CompositionInfo(QWidgetMixin):
    contents = {c.__name__: c for c in [
        CompositionLabel,
        TrackList
    ]}

class TrackInfo(QWidgetMixin):
    contents = {c.__name__: c for c in [

    ]}

class ControlPanel(QWidgetMixin):
    layout_type = QtWidgets.QHBoxLayout
    contents = {c.__name__: c for c in [
        Button1,
        Button2,
        Button3,
    ]}

class MainWidget(QWidgetMixin):
    contents = {c.__name__: c for c in [
        CompositionInfo,
        ControlPanel
    ]}
    contents['label'] = SomeLabel
