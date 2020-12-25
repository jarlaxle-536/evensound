from .base import *
from .registrable import *

class Field:
    def __init__(self, value=None):
        self.default = value
        self.value = value
    def __get__(self, target, owner):
        if target is None:
            return self.default
        dct = target.__dict__
        dct.setdefault(self.__name, self.value)
        return dct[self.__name]
    def __set__(self, target, value):
        target.__dict__[self.__name] = value
        target.update()
    def __set_name__(self, owner, name):
        self.__name = name

class UpdatableMeta(RegistrableMeta):
    def __new__(meta, name, bases, cls_dict):
        "Create field descriptors"
        for field in cls_dict.get('_fields', list()):
            cls_dict[field] = Field(value=cls_dict.get(field))
        return super().__new__(meta, name, bases, cls_dict)

class Updatable(Base, metaclass=UpdatableMeta):
    _fields = list()
    _dependent_on = list()
    _governs = list()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__.update(kwargs)
        self.dependent_on = [self.find(cls_name)
            for cls_name in self._dependent_on]
        for cls in self.dependent_on:
            print(self, 'dep on', cls)
            cls.subscribe(self)
            print(cls, cls._governs)
        self.setup()
    def setup(self):
        self.update()
#        super().setup()
    def update(self):
        for inst in self._governs:
            inst.update()
    @classmethod
    def subscribe(cls, inst):
        cls._governs = cls._governs[:]
        cls._governs += [inst, ]
