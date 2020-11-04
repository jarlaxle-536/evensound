#!/usr/bin/env python

import sys

from logic import *

app = Application()
main_window = MainWindow()
main_window.central_widget = MainWidget().gui
main_window.setCentralWidget(main_window.central_widget)
sys.exit(app.exec_())
