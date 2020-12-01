from logic.loader import *

from logic.gui.widgets import *

class MainWidget(QWidgetMixin):
    contents = {cls.__name__: cls for cls in [
        CompositionTitleLabel
    ]}
