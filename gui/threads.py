import time

from auxiliary import *

class QtThread(QtCore.QThread):
    def run(self):
        while True:
            print(f'{self} cycle')
            if not self.adapter.waiting:
                self.adapter.action()
            time.sleep(self.adapter.period)

class QtThreadAdapter(Singleton):
    waiting = True
    started = False
    period = 0.2
    def setup(self):
        super().setup()
        self.adapt(QtThread(), name='qthread')
    def toggle_activity(self):
        self.waiting = not self.waiting
        if not self.waiting and not self.started:
            self.start()
    def start(self):
        self.started = True
        self.qthread.start()
    def action(self):
        print(f'{self} action')
