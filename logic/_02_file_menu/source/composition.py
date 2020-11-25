from .loader import *

class Composition(Singleton):
    title = GuiConnectedField(
        'Composition title',
        'CompositionTitleRowInput'
    )
    fields = [
        'title'
    ]
