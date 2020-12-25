from .base import *
from .register import *

class RegistrableMeta(BaseMeta):
    def __new__(meta, name, bases, cls_dict):
        obj = super().__new__(meta, name, bases, cls_dict)
        REGISTER.add(obj)
        return obj

class Registrable(Base, metaclass=RegistrableMeta):
    def __init__(self, **kwargs):
        self.create_register_links()
        super().__init__(**kwargs)
    def find(self, cls):
        return REGISTER.find(cls)
    def create_register_links(self):
        self.__dict__.update({f'_{k}': v for k, v in REGISTER.classes.items()})
