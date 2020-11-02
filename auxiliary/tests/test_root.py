import unittest

from auxiliary.general import *


class RootTestCase(unittest.TestCase):
    def test_multiple_inheritance(self):
        class A(Root): adapted_name = 'a'
        class B(Root): adapted_name = 'b'
        class C(A, B): pass
        obj = C()
        for cls in [A, B]:
            self.assertTrue(hasattr(obj, cls.adapted_name))
