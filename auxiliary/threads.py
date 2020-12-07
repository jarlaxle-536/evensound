from .general import *

class QtThread(QtCore.QThread):
    def run(self):
        while True:
            if not self.adapter.waiting:
                self.adapter.action()
            time.sleep(self.adapter.period)

class QtThreadAdapter(Singleton):
    waiting = True
    started = False
    period = 0.2
    def setup(self):
        self.adapt(QtThread(), name='qthread')
        super().setup()
    def toggle_activity(self):
        self.waiting = not self.waiting
        if not self.waiting and not self.started:
            self.start()
    def start(self):
        self.started = True
        self.qthread.start()
    def action(self):
        pass
