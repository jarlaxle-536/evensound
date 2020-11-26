from .loader import *

class Composition(Singleton):
    title = GuiConnectedField(
        'Composition title',
        gui_classes = [
            'CompositionTitleLabel',
            'CompositionTitleRowInput',
        ]
    )
    fields = [
        'title'
    ]
