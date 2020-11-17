import inspect
import sys

class Root(object):
    """Main class to adapt composed elements"""
    instances = dict()
    fields = list()
    def __init__(self, **kwargs):
        for k in self.fields:
            setattr(self, k, kwargs.get(k, getattr(self, k)))
        self.setup()
    def __getattr__(self, attr_name):
        """Single-level adaptation"""
        for k, v in self.__dict__.items():
            res = getattr(v, attr_name, None)
            if not res is None:
                return res
    def setup(self):
        print(f'{self.__class__.__name__} SETUP.')
    def adapt(self, obj, name='adapted', related_name='adapter'):
        setattr(self, name, obj)
        setattr(getattr(self, name), related_name, self)
    @staticmethod
    def find_class(cls_name, modules=['__main__']):
        defined = dict()
        for m in modules:
            defined.update(dict(
                inspect.getmembers(sys.modules[m])
            ))
        return defined.get(cls_name)

class Singleton(Root):
    key = 'object'
    def __new__(cls, *args, **kwargs):
        if not getattr(cls, 'instances'):
            cls.instances = cls.instances.copy()
            cls.instances[Singleton.key] = object.__new__(cls)
        return cls.instances[Singleton.key]
    @staticmethod
    def find(cls_name, obj_id=None, modules=['__main__']):
        cls = Root.find_class(cls_name, modules)
        return cls.instances[Singleton.key]

class EntityMeta(type):
    """Metaclass to simplify connected gui updates"""
    def __new__(cls, clsname, bases, clsdict):
        clsdict = EntityMeta.set_updatable_fields(clsdict)
        return super().__new__(cls, clsname, bases, clsdict)
    def set_updatable_fields(clsdict):
        field_dependencies = clsdict.get('field_dependencies', list())
        for target, source in field_dependencies:
            clsdict[target] = Updater(target=target, source=source)
        return clsdict
    @staticmethod
    def find(cls_name, obj_id=None, modules=['__main__']):
        cls = Root.find_class(cls_name, modules)
        return cls.instances.get(obj_id)

class Entity(Root, metaclass=EntityMeta):
    def __new__(cls, *args, **kwargs):
        print(f'{cls.__name__} new with {args}, {kwargs}')
        obj_id = cls.get_id(kwargs)
        if cls.instances.get(obj_id) is None:
            cls.instances = cls.instances.copy()
            cls.instances[obj_id] = object.__new__(cls)
        return cls.instances[obj_id]

def entity_field_hr(fieldname):
    return fieldname.replace('_', ' ').capitalize()
