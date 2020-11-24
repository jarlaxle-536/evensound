from entities.tests.loader import *

class PointerTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_default_end_pointer(self):
        self.composition = Composition()
        self.composition.insert_beat()
        self.pointer = Pointer()
        self.assertEqual(self.pointer.Composition,
            self.composition)
        self.assertEqual(self.pointer.beat_index,
            len(self.composition.beats))
        self.assertEqual(self.pointer.beat,
            self.composition.beats[-1])
        self.assertEqual(self.pointer.quantum_index,
            self.composition.beats[-1].quantum_number)

if __name__ == '__main__':
    unittest.main()
