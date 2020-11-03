class Entity:
    fields = list()
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
