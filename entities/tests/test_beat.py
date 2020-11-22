from entities.tests.loader import *

class BeatTestCase(unittest.TestCase):
    def setUp(self):
        self.beat = Beat()
    def test_number_of_quants(self):
        MAX_QUANTIZATION_PARAMETER = 2 ** 4
        self.assertEqual(self.beat.quantum_number,
            MAX_QUANTIZATION_PARAMETER * self.beat.time_signature.ratio)

if __name__ == '__main__':
    unittest.main()
