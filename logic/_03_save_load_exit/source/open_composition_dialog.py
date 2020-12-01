from .loader import *

from .composition_file_dialog import *

class OpenCompositionDialog(CompositionFileDialog):
    title = 'Open composition'
    def get_filepath(self):
        self.filepath = self.getOpenFileName(
            self.widget.gui, self.title, FILES_DIR, options=self.options)[0]
        self.State.load(self.filepath)
