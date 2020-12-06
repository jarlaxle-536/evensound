from .loader import *

class State(Singleton):
    def __str__(self):
        return f'<STATE>'

class StateLabel(QLabel):
    def update(self):
        print(self._State)
        self.text = str(self._State.object())
        super().update()
