from .gui_init import *

def init_test_app(unittest_instance):
    gui_dict = create_gui_dict()
    unittest_instance.__dict__.update(gui_dict)

def test_attribute_toggled(ut, attr_meth, func, initial_value=False):
    ut.assertEqual(attr_meth.__call__(), initial_value)
    func.__call__()
    ut.assertEqual(attr_meth.__call__(), not initial_value)
