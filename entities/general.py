from auxiliary import *
from .state import *

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

class Entity(Root, metaclass=EntityMeta):
    instances = dict()
    connected_guis = list()
    def __new__(cls, *args, **kwargs):
        print(f'{cls.__name__} new with {args}, {kwargs}')
        obj_id = cls.get_id(kwargs)
        if cls.instances.get(obj_id) is None:
            cls.instances = cls.instances.copy()
            cls.instances[obj_id] = object.__new__(cls)
        return cls.instances[obj_id]

def entity_field_hr(fieldname):
    return fieldname.replace('_', ' ').capitalize()

class StateMixin(Root):
    def setup(self):
        self.state = State()
