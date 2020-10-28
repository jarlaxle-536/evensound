#!/usr/bin/env python

import sys

from auxiliary import *
from gui import *

app = Application()
main_window = MainWindow()
main_widget = MainWidget()
main_window.central_widget = main_widget
main_window.setCentralWidget(main_window.central_widget.gui)
sys.exit(app.exec_())
