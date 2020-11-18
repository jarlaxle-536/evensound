from entities.tests.loader import *

class MidiOutputTestCase(unittest.TestCase):
    def setUp(self):
        self.device_nums = MidiOutput.device_num_choices
    def test_outputs(self):
        """If no sound is heard, some problems are present"""
        pitch_code = 42
        for device_number in self.device_nums:
#            try:
            current_output = MidiOutput(device_number=device_number)
            current_output.set_instrument(30)
            current_output.note_on(pitch_code, 127)
            time.sleep(0.1)
            current_output.note_off(pitch_code, 127)
#            except Exception as exc:
#                print(device_number)

if __name__ == '__main__':
    unittest.main()
