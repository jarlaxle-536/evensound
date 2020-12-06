from logic._01_app_init import *

def start():
    gui_dict = {cls.__name__: cls.__call__() for cls in [
        Application,
        MainWindow,
        MainWidget
    ]}
    gui_dict['MainWindow'].setCentralWidget(gui_dict['MainWidget'].gui)
    print('OK')
    sys.exit(gui_dict['Application'].exec_())

start()
