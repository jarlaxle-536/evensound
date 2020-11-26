from setuptools import find_packages
import inspect
import sys

from logic.auxiliary import *

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

# import everything from final functionality package
version_number = 3
module_name = [m for m in find_packages()
    if m.startswith(f'logic._{str(version_number).zfill(2)}') and
    m.count('.') == 1][0].split('logic.')[-1]
exec(f'from .{module_name} import *')
