class BaseMeta(type):
    pass

class Base(metaclass=BaseMeta):
    def __init__(self, **kwargs):
        print(f'{self} INIT, {kwargs}')
