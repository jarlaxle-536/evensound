from .loader import *

def alternate(track_obj, beat_obj):
    beat_obj.sounds = [
        Sound(
            pitch=random.randint(40, 80),
            track=track_obj
        )
    for i in range(4)]
