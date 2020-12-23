from logic.loader import *

class PlayController(Singleton):
    _fields = ['playing', 'speed']
    playing = False
    speed = 1
    def toggle(self):
        self.playing = not self.playing

class PlayerControlPanel(QWidget):
    _layout_type = QtWidgets.QHBoxLayout
    _widgets = [
        'PlayButton',
        'Btn1',
        'Btn2',
        'Btn3',
        'Btn4',
    ]

class PlaySpeedButton(QPushButton):
    _dependent_on = ['PlayController', ]
    def update(self):
        self.setEnabled(self.is_enabled())
        self.text = self.get_text()
        super().update()
    def is_enabled(self):
        return PlayController.object().speed != self.speed_level
    def get_text(self):
        return f'Speed: {self.speed_level} X'
    def action(self):
        PlayController.object().speed = self.speed_level

class PlayButton(QPushButton):
    _dependent_on = ['PlayController', ]
    def update(self):
        self.text = self.get_text()
        super().update()
    def get_text(self):
        data = PlayController.object().data
        return {True: 'Stop', False: 'Play'}.get(data['playing'])
    def action(self):
        PlayController.object().toggle()

class Btn1(PlaySpeedButton):
    speed_level = 0.5

class Btn2(PlaySpeedButton):
    speed_level = 1

class Btn3(PlaySpeedButton):
    speed_level = 1.5

class Btn4(PlaySpeedButton):
    speed_level = 2.0

PlayController()
