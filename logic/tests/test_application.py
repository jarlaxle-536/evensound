from logic.tests.loader import *

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    def test_keys(self):
        for key in ['gui', 'state']:
            self.assertTrue(hasattr(self.app, key))

if __name__ == '__main__':
    unittest.main()
