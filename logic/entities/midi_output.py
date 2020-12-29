from logic.loader import *

from .container import *

class MIDIOutput(Entity):
    _fields = ['dev_num', 'output', 'info']
    dev_num = output = info = None
    def setup(self):
        super().setup()
        self.adapt(self.output_obj, name='output')
    def __str__(self):
        return str(self.info)

class MIDIOutputContainer(Container):
    _cls = MIDIOutput
