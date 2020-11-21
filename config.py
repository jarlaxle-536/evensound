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

# QUANTIZATION

QUANIZATION_LEVELS = [2 ** i for i in range(2, 6)]
DEFAULT_QUANTIZATION_LEVEL = QUANIZATION_LEVELS[-1]
