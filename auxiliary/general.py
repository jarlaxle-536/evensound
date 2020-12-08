import sys

from .loader import *
from .register import *

class GeneralMeta(type):
    pass

class RegistrableMeta(GeneralMeta):
    def __new__(meta, name, bases, cls_dict):
        obj = super().__new__(meta, name, bases, cls_dict)
        REGISTER.add(obj)
        return obj

class Registrable(metaclass=RegistrableMeta):
    def __init__(self, **kwargs):
        self.create_register_links()
        super().__init__(**kwargs)
    def create_register_links(self):
        self.__dict__.update({f'_{k}': v for k, v in REGISTER.classes.items()})

class Adaptable:
    _adapted = set()
    def adapt(self, obj, name=None):
        name = name or obj.__class__.__name__
        setattr(self, name, obj)
        setattr(obj, 'adapter', self)
        self._adapted = self._adapted.copy()
        self._adapted.add(name)
    def __getattr__(self, attr_name):
        for adapted_name in self.__dict__.get('_adapted', list()):
            found = getattr(getattr(self, adapted_name), attr_name)
            if not found is None:
                return found

class EntifiableMeta(RegistrableMeta):
    def __new__(meta, name, bases, cls_dict):
        for base in bases:
            for key, value in base.__dict__.items():
                cls_dict.setdefault(key, value)
        for field in cls_dict.get('_fields', list()):
            cls_dict[field] = Field(value=cls_dict.get(field))
        obj = super().__new__(meta, name, bases, cls_dict)
        return obj

class Field:
    _subscripted = set()
    def __init__(self, value=None):
        print(self, value)
        self.value = value
    def __get__(self, target, owner):
        print('get', self, target, owner)
        if target is None: return self
        dct = target.__dict__
        dct.setdefault(self.__name, self.value)
        return dct[self.__name]
    def __set__(self, target, value):
        target.__dict__[self.__name] = value
        for obj in self._subscripted:
            obj.update()
    def __set_name__(self, owner, name):
        self.__name = name
    def subscript(self, obj):
        self._subscripted = self._subscripted.copy()
        self._subscripted.add(obj)

class Entifiable(metaclass=EntifiableMeta):
    _instances = dict()
    _fields = list()
    def __new__(cls, **kwargs):
        obj_id = cls.get_id(kwargs)
        if cls._instances.get(obj_id) is None:
            cls._instances = cls._instances.copy()
            cls._instances[obj_id] = object.__new__(cls)
            return cls._instances[obj_id]
    def __init__(self, **kwargs):
        print(f'{self} INIT.')
        super().__init__(**kwargs)
        self.setup()
    def setup(self):
        print(f'{self} SETUP')
        self.update()
    def update(self):
        print(f'{self} UPDATE')
    @classmethod
    def get_or_create(cls, **kwargs):
        obj_id = cls.get_id(kwargs)
        obj = cls(**kwargs)
        created = not obj is None
        obj = cls._instances[obj_id]
        return obj, created

class Subscriptable:
    _subscriptions = set()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for cls_name, attr_name in self._subscriptions:
            field = getattr(getattr(self, f'_{cls_name}'), attr_name)
            assert isinstance(field, Field)
            field.subscript(self)

class Root(Registrable, Adaptable, Entifiable, Subscriptable):
    def __str__(self):
        return f'<{self.__class__.__name__}>'

class Entity(Root):
    @classmethod
    def get_id(cls, kwargs):
        current_id = 0
        while True:
            if current_id not in cls.instances:
                return current_id
            current_id += 1

class Singleton(Root):
    key = 'object'
    @classmethod
    def get_id(cls, kwargs):
        return cls.key
    @classmethod
    def object(cls):
        return cls._instances.get(cls.key)
