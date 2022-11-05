#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
import cgitb
from db import DB
from obtener import  obtenerViaje, obtenerInformacionViaje
cgitb.enable()

print("Content-type: text/html; charset=UTF-8")
print("")
sys.stdout.reconfigure(encoding='utf-8')

# Conexión a base de datos
db = DB('localhost', 'root', '', 'tarea2')

informacion = ""
volver = ""

form = cgi.FieldStorage()
# si está el parámetro id y es un número
if "id" in form and form["id"].value.isdigit():
    id = int(form["id"].value)
    sqlRes = obtenerViaje(id, db)
    informacion_viaje = obtenerInformacionViaje(sqlRes, db)
    campos = ["País origen", "Ciudad origen", "País destino", "Ciudad destino", "Fecha ida", "Fecha regreso", "Espacio disponible", "Kilos disponibles", "Email", "Celular"]
    for i in range(len(informacion_viaje)):
        informacion += f'''
                        <tr> <th> {campos[i]} </th>
                        <td> {informacion_viaje[i]} </td> </tr>
                        '''
    # si hay una página de referencia a la que volver
    if "p" in form and form["p"].value.isdigit():
        p = int(form["p"].value)
    else:
        p = 1

    volver = f'''<button class="w3-button w3-left w3-light-grey" onclick="window.location='ver-viajes.py?page={p}';">Volver</button>'''



with open("static/informacion-viaje.html", 'r', encoding="utf-8") as template:
    file = template.read()
    print(file.format(informacion, volver))
    
