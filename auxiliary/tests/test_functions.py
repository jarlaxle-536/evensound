from auxiliary.tests.loader import *

class RootTestCase(unittest.TestCase):
    def test_insert_into_list(self):
        self.assertEqual(insert_into_list([], 0), [0])
        self.assertEqual(insert_into_list([], 0, 100), [0])
        self.assertEqual(insert_into_list([0, 1, 2], 0), [0, 1, 2, 0])

if __name__ == '__main__':
    unittest.main()
