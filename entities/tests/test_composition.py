from entities.tests.loader import *

class CompositionTestCase(unittest.TestCase):
    def setUp(self):
        self.composition = Composition()
#        self.original_state_dict = self.state.__dict__.copy()
#        self.test_filepath = os.path.join(
#            os.path.dirname(os.path.abspath(__file__)), 'state.cmp')
    def tearDown(self):
#        if os.path.exists(self.test_filepath):
#            os.remove(self.test_filepath)
        pass
    def test_creation(self):
#        self.state.save(self.test_filepath)
#        self.state.load(self.test_filepath)
#        self.assertEqual(self.original_state_dict, self.state.__dict__)
        pass

if __name__ == '__main__':
    unittest.main()
