from auxiliary import *

class QAction(GuiAdapter):
    _gui_constructor = QtWidgets.QAction
    text = 'Action'
    def setup(self):
        super().setup()
        self.setText(self.text)
        self.triggered.connect(self.action)
    def action(self):
        pass
