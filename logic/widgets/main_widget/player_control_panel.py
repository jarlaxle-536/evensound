from logic.loader import *

from logic.entities import *

class PlayerController(Singleton):
    _fields = ['speed']
    speed = 0
    def setup(self):
        super().setup()
        self.adapt(Player(), name='player')

class PlayerControlPanel(QWidget):
    _layout_type = QtWidgets.QHBoxLayout
    _widgets = [
        'StopButton',
        'PlayButton',
    ]
    def setup(self):
        super().setup()
        self.setFixedWidth(800)

class PlaySpeedButton(QPushButton):
    _dependent_on = ['PlayerController', ]
    def update(self):
        self.setEnabled(self.is_enabled())
        self.text = self.get_text()
        super().update()
    def is_enabled(self):
        return PlayerController.object().speed != self.speed_level
    def get_text(self):
        return f'Play at speed: {self.speed_level} X'
    def action(self):
        PlayerController.object().speed = self.speed_level

class StopButton(PlaySpeedButton):
    speed_level = 0
    def get_text(self):
        return f'Stop'

class PlayAtHalfSpeedButton(PlaySpeedButton):
    speed_level = 0.5

class PlayButton(PlaySpeedButton):
    speed_level = 1

class PlayAtSesquialteralSpeedButton(PlaySpeedButton):
    speed_level = 1.5

class PlayAtDoubleSpeedButton(PlaySpeedButton):
    speed_level = 2.0

PlayerController()
