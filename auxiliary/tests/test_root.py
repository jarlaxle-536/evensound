import unittest

from auxiliary.general import *

class RootTestCase(unittest.TestCase):
    def test_multiple_inheritance(self):
        class A(Root):
            def setup(self, **kwargs):
                self.a = kwargs.get('a', 1)
        class B(Root):
            def setup(self, **kwargs):
                self.b = kwargs.get('b', 2)
        class C(A, B): pass
        obj = C()
        for s in 'ab':
            self.assertTrue(s in obj.__dict__)
