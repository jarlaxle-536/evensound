from .entity import *
from .singleton import *

class Queryset(Singleton):
    entity_cls = None
    min_size = 0
    max_size = 10 ** 6
    contents = list()
    def update(self):
        super().update()
        self.set_contents()
    def setup(self):
        self.connect_to_entity()
        super().setup()
    def connect_to_entity(self):
        print(f'{self}:connect_to_entity "{self.entity_cls}"')
        entity_cls = self.find(self.entity_cls)
        assert entity_cls is not None, f"{self} is not linked to entity!"
        self.adapt(entity_cls, name='entity')
    def set_contents(self):
        self.contents = {k: v for k, v in self.entity._instances.items()
            if self.condition(v)}
    def condition(self, inst):
        return True
    def get_instance(self, id=None):
        return self.contents.get(id, DummyModel.get_or_create()[0])

class DummyModel(Singleton):
    def __getattr__(self, attr_name):
        print(f'{self}:getattr {attr_name}')
        return lambda *args, **kwargs: None
