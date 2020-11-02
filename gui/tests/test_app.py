from gui import *

def _test():
    app = Application()
    for key in ['gui', 'state']:
        assert hasattr(app, key)

_test()
