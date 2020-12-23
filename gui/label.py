from gui.loader import *

class QLabel(GuiAdapter):
    _gui_constructor = QtWidgets.QLabel
    text = 'Label'
    def update(self):
        super().update()
        self.setText(self.text)
