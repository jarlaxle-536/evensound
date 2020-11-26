from auxiliary import *

def create_gui_dict():
    dct = dict()
    for cls_name in GUI_CLASSES:
        cls = Root.find_class(cls_name)
        obj = cls.instances['object'] if cls.instances else cls.__call__()
        dct[cls_name] = obj
    print(dct)
    return dct

GUI_CLASSES = [
    'Application',
    'MainWindow',
    'MainWidget'
]
