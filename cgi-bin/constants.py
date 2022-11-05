# -*- coding: utf-8 -*-

import re

# RegEx
REGEX_FECHA = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$')
REGEX_EMAIL = re.compile(r'^[^@]+@[^@]+\.[a-zA-Z]{2,}$')
REGEX_NUMERO = re.compile(r'^(\+)[0-9]{10,15}$')


CAMPOS_VIAJE = ["pais-origen", "ciudad-origen", "pais-destino", "ciudad-destino", "fecha-ida",
                "fecha-regreso", "espacio-disponible", "kilos-disponibles", "email", "celular"]

CAMPOS_ENCARGO = ["descripcion", "espacio-solicitado", "kilos-solicitados", "pais-origen", "ciudad-origen", "pais-destino", 
                  "ciudad-destino", "foto-encargo-1",  "foto-encargo-2",  "foto-encargo-3", "email", "celular"]

# Tamaño máximo de foto permitida
MAX_FILE_SIZE = 10000000 # 100 KB
