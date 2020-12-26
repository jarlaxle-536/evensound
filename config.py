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

QUANTIZATION_PARAMETERS = [2 ** i for i in range(1, 5)]
MAX_QUANTIZATION_PARAMETER = QUANTIZATION_PARAMETERS[-1]
DEFAULT_QUANTIZATION_PARAMETER = QUANTIZATION_PARAMETERS[-1]
