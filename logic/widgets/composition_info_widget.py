from logic.loader import *

from .composition_label import *

class CompositionInfoWidget(QWidgetMixin):
    contents = {c.__name__: c for c in [
        CompositionLabel,
    ]}
