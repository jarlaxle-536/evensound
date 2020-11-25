import sys

# import everything from final functionality package
from ._02_file_menu import *

def start_app():
    app = LOGIC_DICT['application_class']()
    main_window = LOGIC_DICT['main_window_class']()
    main_window.central_widget = LOGIC_DICT['main_widget_class']().gui
    main_window.setCentralWidget(main_window.central_widget)
    sys.exit(app.exec_())
