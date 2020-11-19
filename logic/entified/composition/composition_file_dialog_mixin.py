from logic.general import *

class CompositionFileDialogMixin(FileDialogMixin):
    ext = 'cmp'
    name_filters = ['Composition (*.cmp)', ]
    def setup(self):
        super().setup()
        self.setNameFilters(self.name_filters)
        self.setDefaultSuffix(self.ext)
