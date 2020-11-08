from gui import *

class CompositionDialogMixin(FileDialogMixin):
    ext = 'cmp'
    name_filters = ['Composition (*.cmp)', ]
    def setup(self):
        super().setup()
        self.setNameFilters(self.name_filters)
        self.setDefaultSuffix(self.ext)

class OpenCompositionDialogMixin(CompositionDialogMixin):
    def get_filepath(self):
        self.filepath = self.getOpenFileName(
            self.widget.gui, self.title, FILES_DIR, options=self.options)[0]

class SaveCompositionDialogMixin(CompositionDialogMixin):
    def get_filepath(self):
        self.filepath = self.getSaveFileName(
            self.widget.gui, self.title, FILES_DIR, options=self.options)[0]

class OpenCmpDialog(OpenCompositionDialogMixin):
    title = 'Open file'

class SaveCmpDialog(SaveCompositionDialogMixin):
    title = 'Save file'
