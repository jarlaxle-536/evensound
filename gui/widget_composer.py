from gui.loader import *

class WidgetComposer(Root):
    _widgets = list()
    _contents = dict()
    def compose(self, composing_func):
        for cls_name in self._widgets:
            obj, created = REGISTER.find(cls_name).get_or_create()
            composing_func.__call__(obj.gui)
            self._contents = self._contents.copy()
            self._contents[cls_name] = (len(self._contents), obj)
