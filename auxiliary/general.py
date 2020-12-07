import sys

from .loader import *
from .register import *

class RootMeta(type):
    def __new__(meta, name, bases, cls_dict):
        obj = super().__new__(meta, name, bases, cls_dict)
        REGISTER.add(obj)
        return obj

class Root(metaclass=RootMeta):
    _adapted = set()
    _governed = set()
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.create_register_links()
        self.setup()
    def create_register_links(self):
        self.__dict__.update({f'_{k}': v for k, v in REGISTER.classes.items()})
    def setup(self):
        print(f'{self.__class__.__name__} SETUP')
        self.update()
    def update(self):
        for cls in self._governed:
            for inst_obj in cls.instances.values():
                inst_obj.update()
        print(f'{self.__class__.__name__} UPDATE')
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

class Entity(Root):
    instances = dict()
    _dependent = set()
    def __new__(cls, **kwargs):
        print(f'creating {cls} object, which depends on {cls._dependent} and governs {cls._governed}')
        classes = REGISTER.get(*cls._dependent)
        for dep_class in classes:
            dep_class._governed = dep_class._governed.copy()
            dep_class._governed.add(cls)
            print(dep_class, dep_class._governed)
        obj_id = cls.get_id(kwargs)
        if cls.instances.get(obj_id) is None:
            cls.instances = cls.instances.copy()
            cls.instances[obj_id] = object.__new__(cls)
            return cls.instances[obj_id]
    @classmethod
    def get_or_create(cls, **kwargs):
        obj_id = cls.get_id(kwargs)
        obj = cls(**kwargs)
        created = not obj is None
        obj = cls.instances[obj_id]
        return obj, created
    @classmethod
    def get_id(cls, kwargs):
        current_id = 0
        while True:
            if current_id not in cls.instances:
                return current_id
            current_id += 1

class Singleton(Entity):
    key = 'object'
    @classmethod
    def get_id(cls, kwargs):
        return cls.key
    @classmethod
    def object(cls):
        return cls.instances.get(cls.key)
