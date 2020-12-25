from gui.loader import *

class QListWidget(GuiAdapter):
    _gui_constructor = QtWidgets.QListWidget
    _index = -1
    items = list()
    def update(self):
        self.clear()
        for item in self.items:
            self.addItem(self.get_repr(item))
#        self.setCurrentRow(self._index)
    def setup(self):
        super().setup()
        self.currentRowChanged.connect(self.on_change)
    def on_change(self, index):
        print(f'{self}:on_change {index}')
        self._index = index
        print(f'{self} new index: {self._index}')
    def get_repr(self, dct):
        return str(dct)
