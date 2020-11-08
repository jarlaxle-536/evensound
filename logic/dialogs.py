from gui import *

class CompositionFileDialogMixin(FileDialogMixin):
    ext = 'cmp'
    name_filters = ['Composition (*.cmp)', ]
    def setup(self):
        super().setup()
        self.setNameFilters(self.name_filters)
        self.setDefaultSuffix(self.ext)

class OpenCompositionDialogMixin(CompositionFileDialogMixin):
    def get_filepath(self):
        self.filepath = self.getOpenFileName(
            self.widget.gui, self.title, FILES_DIR, options=self.options)[0]

class SaveCompositionDialogMixin(CompositionFileDialogMixin):
    def get_filepath(self):
        self.filepath = self.getSaveFileName(
            self.widget.gui, self.title, FILES_DIR, options=self.options)[0]

class OpenCmpDialog(OpenCompositionDialogMixin):
    title = 'Open file'

class SaveCmpDialog(SaveCompositionDialogMixin):
    title = 'Save file'

class NewCompositionDialog(QDialogMixin):
    title = 'New composition'

class AddTrackDialog(QDialogMixin):
    title = 'Add track'
