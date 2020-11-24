from entities.tests.loader import *

class BeatTestCase(unittest.TestCase):
    def setUp(self):
        self.beat = Beat()
    def tearDown(self):
        del self.beat
    def test_time_signature_passed(self):
        for ts_num, ts_den, ratio in [
            (4, 4, 1),
            (6, 4, 1.5),
            (7, 4, 1.75)
        ]:
            self.beat = Beat(ts_numerator=ts_num, ts_denominator=ts_den)
            self.assertEqual(
                [getattr(self.beat.time_signature, f) for f in [
                    'numerator',
                    'denominator',
                    'ratio'
                ]], [ts_num, ts_den, ratio])
    def test_number_of_quants(self):
        for quant_level in range(6):
            quant_parameter = 2 ** quant_level
            self.beat.quantization_parameter = quant_parameter
            self.assertEqual(self.beat.quantum_number,
                quant_parameter * self.beat.time_signature.ratio)

if __name__ == '__main__':
    unittest.main()
