import random

from logic.loader import *

class ChangeTitleButton(QPushButton):
    text = 'change title'
    def action(self):
        self._Composition.object().title = str(random.randint(1, 1000))
