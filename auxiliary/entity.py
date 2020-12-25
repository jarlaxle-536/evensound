from .root import *

class EntityMeta(UpdatableMeta):
    def __new__(meta, name, bases, cls_dict):
        "Replicate instances for deep hierarchy"
        cls_dict['_instances'] = dict()
        return super().__new__(meta, name, bases, cls_dict)

class Entity(Root, metaclass=EntityMeta):
    _instances = dict()
    def __new__(cls, **kwargs):
        obj_id = cls.get_id(**kwargs)
        if cls._instances.get(obj_id) is None:
            obj = object.__new__(cls)
            cls._instances[obj_id] = obj
            cls._instances[obj_id].id = obj_id
            return cls._instances[obj_id]
    @classmethod
    def get_id(cls, **kwargs):
        return len(cls._instances)
    @classmethod
    def get_or_create(cls, **kwargs):
#        print(f'{cls}:get_or_create with {kwargs}')
        obj_id = cls.get_id(**kwargs)
        obj = cls(**kwargs)
        created = not obj is None
        obj = cls._instances[obj_id]
        return obj, created
    @property
    def data(self):
        res = {f: getattr(self, f) for f in self._fields}
        res['id'] = self.id
        res['object'] = self
        return res
