import unittest

from auxiliary.general import *

class RootTestCase(unittest.TestCase):
    def setUp(self):
        class A(Root):
            def __init__(self, **kwargs):
                self.a = kwargs.get('a', 1)
                super().__init__(**kwargs)
        class B(Root):
            def __init__(self, **kwargs):
                self.b = kwargs.get('b', 2)
                super().__init__(**kwargs)
        class C(A, B):
            pass
        class D(Root):
            def __init__(self, **kwargs):
                self.d = kwargs.get('d', 3)
                super().__init__(**kwargs)
        class E(Root):
            def __init__(self, **kwargs):
                self.e = kwargs.get('e', 4)
                super().__init__(**kwargs)
        class F(D, E):
            pass
        class G(C, F):
            pass
        self.classes = {cls.__name__: cls for cls in [A, B, C, D, E, F, G]}
    def test_multiple_inheritance1(self):
        obj = self.classes['C']()
        for s in 'ab':
            self.assertTrue(s in obj.__dict__)
    def test_multiple_inheritance2(self):
        obj = self.classes['G']()
        print(obj.__dict__)
#        for s in 'abde':
#            self.assertTrue(s in obj.__dict__)
