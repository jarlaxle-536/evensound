from logic.loader import *

from logic.entities import *

class PlayerController(Singleton):
    _dependent_on = ['Player']
    _fields = ['speed']
    speed = 0
    def set_speed(self, speed_level):
        print(f'{self}:set_speed {speed_level}')
        self.speed = speed_level
        self._Player.object().set_speed(speed_level)

class PlayerControlPanel(QWidget):
    _layout_type = QtWidgets.QHBoxLayout
    _widgets = [
        'PlayerInfoLabel',
        'StopButton',
        'PlayButton',
    ]
    def setup(self):
        super().setup()
        self.setFixedWidth(800)

class PlayerInfoLabel(QLabel):
    _dependent_on = ['PlayerController', ]
    def update(self):
        self.text = str(Player.object())
        super().update()

class PlaySpeedButton(QPushButton):
    _dependent_on = ['PlayerController', ]
    def update(self):
        self.setEnabled(self.is_enabled())
        self.text = self.get_text()
        super().update()
    def is_enabled(self):
        return self._PlayerController.object().speed != self.speed_level
    def get_text(self):
        return f'Play at speed: {self.speed_level} X'
    def action(self):
        self._PlayerController.object().set_speed(self.speed_level)

class StopButton(PlaySpeedButton):
    speed_level = 0
    def action(self):
        super().action()
        self._Player.object().time = self._Player.time
    def get_text(self):
        return 'Stop'

class PlayButton(PlaySpeedButton):
    speed_level = 1
    def get_text(self):
        return 'Play'

PlayerController()
