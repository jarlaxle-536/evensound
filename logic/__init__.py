from setuptools import find_packages
import inspect
import sys

from logic.auxiliary import *

from logic.gui import *

def start_app():
    gui_dict = create_gui_dict()
    app, main_window, main_widget = [gui_dict[k] for k in [
        'Application',
        'MainWindow',
        'MainWidget'
    ]]
    main_window.central_widget = main_widget.gui
    main_window.setCentralWidget(main_window.central_widget)
    sys.exit(app.exec_())
