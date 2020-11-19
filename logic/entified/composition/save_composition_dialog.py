from .composition_file_dialog_mixin import *

class SaveCompositionDialogMixin(CompositionFileDialogMixin):
    def get_filepath(self):
        self.filepath = self.getSaveFileName(
            self.widget.gui, self.title, FILES_DIR, options=self.options)[0]

class SaveCmpDialog(SaveCompositionDialogMixin):
    title = 'Save file'
