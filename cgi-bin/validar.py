# -*- coding: utf-8 -*-

import os
import re
import constants as cons
from datetime import datetime


class Validador():

    def __init__(self, db):
        self.errores = []
        self.db = db

    # Valida que cada ciudad esté asociada al país en la base de datos y que no posean la misma ciudad de origen y destino
    def validarPaisCiudad(self, pais_origen, ciudad_origen, pais_destino, ciudad_destino):
        var = []
        if pais_origen == "Elija ...":
            var += ["Seleccione país de origen."]
        if ciudad_origen == "Elija ...":
            var += ["Seleccione ciudad de origen."]
        if not var:
            sql = f"SELECT ciudad.nombre FROM pais JOIN ciudad ON pais.id=ciudad.pais WHERE pais.nombre='{pais_origen}'"
            if self.db.obtener_data(sql)[0][0] != ciudad_origen:
                self.errores += [f"La ciudad origen {ciudad_origen} no pertence al país origen {pais_origen}."]
        self.errores += var
        var = []
        if pais_destino == "Elija ...":
            var += ["Seleccione país de destino."]
        if ciudad_destino == "Elija ...":
            var += ["Seleccione ciudad de destino."]
        if not var:
            sql = f"SELECT ciudad.nombre FROM pais JOIN ciudad ON pais.id=ciudad.pais WHERE pais.nombre='{pais_destino}'"
            if self.db.obtener_data(sql)[0][0] != ciudad_destino:
                self.errores += [f"La ciudad destino {ciudad_destino} no pertence al país destino {pais_destino}."]
            if ciudad_origen == ciudad_destino:
                self.errores += ["La ciudad origen no puede ser la misma que la ciudad destino."]
        self.errores += var

    # Valida que las fechas de ida y regreso estén en formato aaaa-mm-dd y que la fecha de ida este antes que la fecha de regreso.
    def validarFecha(self, fechaIda, fechaRegreso):
        var = []
        if not re.fullmatch(cons.REGEX_FECHA, fechaIda):
            var += ["La fecha de ida no cumple con el fomato aaaa-mm-dd."]
        if not re.fullmatch(cons.REGEX_FECHA, fechaRegreso):
            var += ["La fecha de regreso no cumple con el fomato aaaa-mm-dd."]
        if not var:
            if datetime.fromisoformat(fechaIda).timestamp() >= datetime.fromisoformat(fechaRegreso).timestamp():
                self.errores += ["La fecha de regreso tiene que ser posterior a la fecha de ida."]
        self.errores += var

    # Valida que el espacio escogidos estén en la lista.
    def validarEspacio(self, espacio):
        if espacio not in ["10x10x10", "20x20x20", "30x30x30"]:
            self.errores += ["No se ha seleccionado espacio."]

    # Valida que los kilos escogidos estén en la lista.
    def validarKilos(self, kilos):
        if kilos not in ["500 gr", "800 gr", "1 kg", "1.5 kg", "2 kg"]:
            self.errores += ["No se ha seleccionado kilos."]

    # Valida que el email y el celular (si es que hay), estén en un formato apropiado.
    def validarContactos(self, email, celular):
        if not re.fullmatch(cons.REGEX_EMAIL, email):
            self.errores += ["El email no tiene un formato válido."]
        if celular != "":
            if not re.fullmatch(cons.REGEX_NUMERO, celular):
                self.errores += ["El celular no tiene un formato válido."]

    def validarDescripcion(self, descripcion):
        if descripcion == "":
            self.errores += ["No se ha agregado descripcion."]
        if len(descripcion) > 250:
            self.errrores += ["La descripción es demasiado larga."]

    # Valida que los archivos tengan el formato png, jpg o jpeg, ademas de tener un tamaño máximo definido.
    def validarArchivo(self, archivo):
        if archivo == "":
            return
        if archivo.filename:
            tipos_soportados = ['image/jpeg', 'image/jpg', 'image/png']
            try:
                # averiguar el tipo real
                tipo = archivo.type
                if tipo in tipos_soportados:
                    # averiguar tamaño
                    size = os.fstat(archivo.file.fileno()).st_size
                    if size > cons.MAX_FILE_SIZE:
                        self.errores += [f"El archivo {archivo.filename} es muy grande."]
                else:
                    self.errores += [f"El formato del archivo {archivo.filename} no es válido."]
            except:
                self.errores += [f"No se pudo validar el archivo {archivo.filename}."]

    # Valida que al menos se haya seleccionado un archivo, y en el caso se hacerlo, valida dicho archivo.
    def validarArchivos(self, archivo_1, archivo_2, archivo_3):
        # Si al menos hay un archivo subido
        if (archivo_1 != "" or archivo_2 != "" or archivo_3 != ""):
            self.validarArchivo(archivo_1) 
            self.validarArchivo(archivo_2) 
            self.validarArchivo(archivo_3) 
        else:
            self.errores += ["No se ha seleccionado ningún archivo."]


# Valida las respuestas proporcionadas para un viaje.
def validarViaje(respuestas, db):
    validador = Validador(db)
    validador.validarPaisCiudad(respuestas[0], respuestas[1], respuestas[2], respuestas[3])
    validador.validarFecha(respuestas[4], respuestas[5])
    validador.validarEspacio(respuestas[6])
    validador.validarKilos(respuestas[7])
    validador.validarContactos(respuestas[8], respuestas[9])
    return validador.errores

# Valida las respuestas proporcionadas para un encargo.
def validarEncargo(respuestas, db):
    validador = Validador(db)
    validador.validarDescripcion(respuestas[0])
    validador.validarEspacio(respuestas[1])
    validador.validarKilos(respuestas[2])
    validador.validarPaisCiudad(respuestas[3], respuestas[4], respuestas[5], respuestas[6])
    validador.validarArchivos(respuestas[7], respuestas[8], respuestas[9])
    validador.validarContactos(respuestas[10], respuestas[11])
    return validador.errores
