from .loader import *
from .new_composition_action import *

class FileMenu(QMenuMixin):
    title = 'File'
    actions_list = [
        NewCompositionAction,
    ]
