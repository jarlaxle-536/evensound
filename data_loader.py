import json
import os

from config import *



# NOTES, SCALES, etc

with open(NOTES_FILEPATH) as file:
    NOTES = json.load(file)
