from logic.loader import *

class CompositionPureEntity(Singleton):
    title = 'Composition title'
    fields = [
        'title'
    ]

class Composition(CompositionPureEntity, metaclass=GuiConnectMeta):
    gui_links = {
        'title': [
            'CompositionTitleLabel',
            'CompositionTitleRowInput'
        ]
    }
