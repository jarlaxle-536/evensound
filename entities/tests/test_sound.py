from entities.tests.loader import *

class SoundTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_default_end_pointer(self):
        self.composition = Composition()
        self.pointer = Pointer()
        self.assertEqual(self.pointer.composition,
            self.composition)
        self.assertEqual(self.pointer.beat_index,
            len(self.composition.beats))
        self.assertEqual(self.pointer.beat,
            self.composition.beats[-1])
        self.assertEqual(self.pointer.quantum_index,
            self.composition.beats[-1].quantum_number)

if __name__ == '__main__':
    unittest.main()
