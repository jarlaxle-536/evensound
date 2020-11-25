def init_test_app(instance, logic_dict):
    for attr in gui_classes:
        cls = logic_dict.get(attr)
        obj = cls.instances['object'] if cls.instances else cls.__call__()
        setattr(instance, attr.replace('_class', ''), obj)

def destroy_test_app(instance):
    for attr in gui_classes:
        LOGIC_DICT.get(attr).instances = []

def test_attribute_toggled(ut, attr_meth, func, initial_value=False):
    ut.assertEqual(attr_meth.__call__(), initial_value)
    func.__call__()
    ut.assertEqual(attr_meth.__call__(), not initial_value)

gui_classes = [
    'application_class',
    'main_window_class',
    'main_widget_class'
]
