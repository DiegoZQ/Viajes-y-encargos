#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
import cgitb
from db import DB
from obtener import obtenerListaViajes, obtenerInformacionViaje
cgitb.enable()

print("Content-type: text/html; charset=UTF-8")
print("")
sys.stdout.reconfigure(encoding='utf-8')

# Conexión a base de datos
db = DB('localhost', 'root', '', 'tarea2')

informacion = ""
siguiente = ""
anterior = ""

form = cgi.FieldStorage()
# Si está el parámetro page y es un número
if "page" in form and form["page"].value.isdigit():
    page = int(form["page"].value)
    start = (page-1)*5
    sqlRes = obtenerListaViajes(start, 5, db)
    for fila in sqlRes:
        informacion_viaje = obtenerInformacionViaje(fila, db)
        informacion += f'''<tr class='clickable-row' href='informacion-viaje.py?id={str(fila[0])}&p={page}'>
                    <td>{informacion_viaje[0]}</td><td>{informacion_viaje[2]}</td><td>{informacion_viaje[4]}</td>
                    <td>{informacion_viaje[5]}</td><td>{informacion_viaje[6]}</td><td>{informacion_viaje[7]}</td><td>{informacion_viaje[8]}</td>'''
    # Si quedan más viajes que mostrar
    if obtenerListaViajes(start+5, 1, db):
        siguiente = f'''<button class="w3-button w3-right w3-green" onclick="window.location='ver-viajes.py?page={str(page+1)}';">Siguiente</button>'''
    # Si la página actual es mayor a la primera
    if page > 1:
        anterior = f'''<button class="w3-button w3-right w3-light-grey" onclick="window.location='ver-viajes.py?page={str(page-1)}';">Anterior</button>'''

with open("static/ver-viajes.html", 'r', encoding="utf-8") as template:
    file = template.read()
    print(file.format(informacion, siguiente, anterior))