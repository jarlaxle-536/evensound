class Register:
    classes = dict()
    def __getattr__(self, attr_name):
        obj = self.classes.get(attr_name)
        if not obj:
            print(f'NOT FOUND: {attr_name}.')
            return lambda *args, **kwargs: None
        return obj
    def add(self, *classes):
        self.classes.update({cls.__name__: cls for cls in classes})
    def get(self, *cls_names):
        return tuple([self.classes.get(cls_name) for cls_name in cls_names])        

REGISTER = Register()
