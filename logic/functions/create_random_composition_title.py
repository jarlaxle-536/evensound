from .loader import *

def create_random_composition_title():
    return FAKER.sentence().replace('.', '')
