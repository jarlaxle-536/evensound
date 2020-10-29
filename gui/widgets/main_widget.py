from gui.general import *

class MainWidget(WidgetAdapter):
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            TrackList,
        ]}
        super().setup()

class TrackList(WidgetAdapter):
    def setup(self):
        self.contents = {cls.__name__: cls.__call__() for cls in [
            Label1,
        ]}
        super().setup()

class Label1(LabelAdapter):
    def setup(self):
        self.text = f'composition dict: {self.application.state.composition.__dict__}'
        super().setup()
