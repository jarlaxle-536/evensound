import unittest

from auxiliary.general import *

class EntityTestCase(unittest.TestCase):
    def setUp(self):
        class A(Entity):
            fields = ['a']
            @staticmethod
            def get_id(dct):
                return dct.get('a')
        self.cls = A
    def test_objects_creation(self):
        inst1 = self.cls(a=1)
        inst2 = self.cls(a=1)
        inst3 = self.cls(a=2)
        self.assertEqual(len(self.cls.instances), 2)
        self.assertEqual(inst1, inst2)
        self.assertNotEqual(inst1, inst3)
