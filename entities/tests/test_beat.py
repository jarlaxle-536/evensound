from entities.tests.loader import *

class BeatTestCase(unittest.TestCase):
    def setUp(self):
        self.beat = Beat()
    def test_number_of_quants(self):
        for quant_level in range(6):
            quant_parameter = 2 ** quant_level
            self.beat.quantization_parameter = quant_parameter
            self.assertEqual(self.beat.quantum_number,
                quant_parameter * self.beat.time_signature.ratio)

if __name__ == '__main__':
    unittest.main()
