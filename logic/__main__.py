from logic import *

def start():
    gui_dict = create_gui_dict()
    gui_dict['MainWindow'].setCentralWidget(gui_dict['MainWidget'].gui)
    print('OK')
    sys.exit(gui_dict['Application'].exec_())

start()
