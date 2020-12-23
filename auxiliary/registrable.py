from .base import *
from .register import *

class RegistrableMeta(BaseMeta):
    def __new__(meta, name, bases, cls_dict):
        obj = super().__new__(meta, name, bases, cls_dict)
        REGISTER.add(obj)
        return obj

class Registrable(Base, metaclass=RegistrableMeta):
    def find(self, cls):
        return REGISTER.find(cls)
