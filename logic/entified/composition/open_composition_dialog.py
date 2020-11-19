from .composition_file_dialog_mixin import *

class OpenCompositionDialogMixin(CompositionFileDialogMixin):
    title = 'Open file'
    def get_filepath(self):
        self.filepath = self.getOpenFileName(
            self.widget.gui, self.title, FILES_DIR, options=self.options)[0]
