from entities.tests.loader import *

class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def test_outputs(self):
        """If no sound is heard, no MIDI output is found or it's busy"""
        for device_number in Player.midi_outputs:
            player = Player(midi_device_number=device_number)
            test_midi_output(player.midi_output)
            play_on_midi_output(player.midi_output)

if __name__ == '__main__':
    unittest.main()
