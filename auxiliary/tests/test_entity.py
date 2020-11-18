from auxiliary.tests.loader import *

class A(Entity):
    fields = ['a']
    @staticmethod
    def get_id(dct):
        return dct.get('a')

class B(Entity):
    fields = ['b']
    @staticmethod
    def get_id(dct):
        return dct.get('b')

class EntityTestCase(unittest.TestCase):
    def setUp(self):
        self.classes = [A, B]
    def tearDown(self):
        for cls in self.classes:
            cls.instances = dict()
    def test_objects_creation(self):
        inst1 = A(a=1)
        inst2 = A(a=1)
        inst3 = A(a=2)
        self.assertEqual(len(A.instances), 2)
        self.assertEqual(inst1, inst2)
        self.assertNotEqual(inst1, inst3)
    def test_find(self):
        a = A(a=42)
        self.assertEqual(a, Entity.find('A', obj_id=42,
            modules=['__main__', 'auxiliary.tests.test_entity']))
    def test_no_collision(self):
        a = A(a=1)
        b = B(b=1)
        print(a.__dict__, b.__dict__)
        print(A.instances, B.instances)

if __name__ == '__main__':
    unittest.main()
