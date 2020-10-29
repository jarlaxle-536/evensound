class Instrument:
    # default instrument would be Acoustic Grand Piano
    code = 1
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
