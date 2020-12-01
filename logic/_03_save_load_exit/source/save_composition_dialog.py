from .loader import *

from .composition_file_dialog import *

@singleton_register('State')
class SaveCompositionDialog(CompositionFileDialog):
    title = 'Save composition'
    def get_filepath(self):
        self.filepath = self.getSaveFileName(
            self.widget.gui, self.title, FILES_DIR, options=self.options)[0]
        self.State.save(self.filepath)
