"""Configurations and system variables. to run: uvicorn main:app --reload"""

import os
from schema_functions import init_System

# Inicializando esquema e lista para buscas
elementos = init_System()
local_directory = os.getcwd()
