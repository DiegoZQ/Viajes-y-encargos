#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi 
import cgitb
from db import DB
import constants as cons
from validar import validarEncargo
from obtener import obtenerRespuestas, obtenerRespuestasSQLEncargo
cgitb.enable()

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

# Conexión a base de datos
db = DB('localhost', 'root', '', 'tarea2')

errores = []
alerta = ""
success = False

form = cgi.FieldStorage()


# Revisar si nos hicieron submit
if len(form) > 0:
    respuestas = obtenerRespuestas(form, cons.CAMPOS_ENCARGO)
    errores = validarEncargo(respuestas, db)
    if not errores:
        if db.agregar_encargo(obtenerRespuestasSQLEncargo(respuestas, db)):
            success = True
        else:
            alerta = "<script> alert('No se pudo ingresar los datos.'); </script>"

if success:
    with open("static/switch-page.html", 'r', encoding="utf-8") as template:
        file = template.read()
        print(file.format(**{"location" : "inicio.py?success=2"}))

else:
    with open("static/agregar-encargo.html", 'r', encoding="utf-8") as template:
        file = template.read()
        lista_errores = ""
        for i in range(len(errores)):
            lista_errores += f"<p> {errores[i]} </p>"
        print(file.format(alerta, lista_errores))