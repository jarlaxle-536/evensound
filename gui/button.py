from gui.loader import *

class QPushButton(GuiAdapter):
    _gui_constructor = QtWidgets.QPushButton
    text = 'Button'
    def update(self):
        super().update()
        self.setText(self.text)
    def setup(self):
        super().setup()
        self.clicked.connect(self.action)
    def action(self):
        print(f'{self} clicked.')
