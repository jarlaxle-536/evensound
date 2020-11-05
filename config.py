import json
import os

# PATHS

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(MAIN_DIR, 'data')
FILES_DIR = os.path.join(MAIN_DIR, 'files')

for d in [MAIN_DIR, DATA_DIR, FILES_DIR]:
    if not os.path.exists(d):
        os.mkdir(d)

# GUI

MAX_WINDOW_SIZE = (1400, 800)
