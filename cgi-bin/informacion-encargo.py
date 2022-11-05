#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
import cgitb
from db import DB
from obtener import  obtenerEncargo, obtenerInformacionEncargo
cgitb.enable()

print("Content-type: text/html; charset=UTF-8")
print("")
sys.stdout.reconfigure(encoding='utf-8')

# Conexión a base de datos
db = DB('localhost', 'root', '', 'tarea2')

modales = ""
informacion = ""
volver = ""

form = cgi.FieldStorage()
# si está el parámetro id y es un número
if "id" in form and form["id"].value.isdigit():
    id = int(form["id"].value)
    sqlRes = obtenerEncargo(id, db)
    informacion_encargo = obtenerInformacionEncargo(sqlRes, db)
    fotos = informacion_encargo[8:]

    campos = ["Comentario", "Espacio solicidado", "Kilos solicitados", "País origen", "Ciudad origen", "País destino",
             "Ciudad destino", "Email", "Celular", "Foto 1"]

    if len(fotos) > 1:
        campos += ["Foto 2"]
    if len(fotos) > 2:
        campos += ["Foto 3"]

    for i in range(len(fotos)):
        modales += f'''<div class="modal fade" id="modalFoto{i}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog modal-xl" style="width:90%">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body modal-lg text-center">
                                    <img {fotos[i]} width="1280" height="1024">
                                </div>
                            </div>
                        </div>
                    </div>'''
                            

    
    for i in range(len(informacion_encargo)):
        # caso fotos
        if i > 8:
            informacion_encargo[i] = f'''<img {informacion_encargo[i]} width="640" height="480" data-bs-toggle='modal' data-bs-target='#modalFoto{i-8}'>'''   

        informacion += f'''
                        <tr> <th> {campos[i]} </th>
                        <td> {informacion_encargo[i]} </td> </tr>
                        '''
    # si hay una página de referencia a la que volver
    if "p" in form and form["p"].value.isdigit():
        p = int(form["p"].value)
    else:
        p = 1

    volver = f'''<button class="w3-button w3-left w3-light-grey" onclick="window.location='ver-encargos.py?page={p}';">Volver</button>'''



with open("static/informacion-encargo.html", 'r', encoding="utf-8") as template:
    file = template.read()
    print(file.format(informacion, volver, modales))
    