import unittest

from auxiliary.general import *

class A(Entity):
    fields = ['a']
    @staticmethod
    def get_id(dct):
        return dct.get('a')

class EntityTestCase(unittest.TestCase):
    def setUp(self):
        self.cls = A
    def tearDown(self):
        self.cls.instances = dict()
    def test_objects_creation(self):
        inst1 = self.cls(a=1)
        inst2 = self.cls(a=1)
        inst3 = self.cls(a=2)
        self.assertEqual(len(self.cls.instances), 2)
        self.assertEqual(inst1, inst2)
        self.assertNotEqual(inst1, inst3)
    def test_find(self):
        a = self.cls(a=42)
        self.assertEqual(a, self.cls.find('A', 42,
            modules=['__main__', 'auxiliary.tests.test_entity']))
