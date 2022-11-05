#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi

print("Content-type: text/html; charset=UTF-8")
print("")
sys.stdout.reconfigure(encoding='utf-8')

alerta = ""
datos = cgi.FieldStorage()

if "success" in datos:
    if datos["success"].value == "1":
        alerta = "<script> alert('Viaje agregado exitosamente.'); </script>"
    elif datos["success"].value == "2":
        alerta = "<script> alert('Encargo agregado exitosamente.'); </script>"


with open("static/inicio.html", 'r', encoding="utf-8") as template:
    file = template.read()
    print(file.format(alerta))