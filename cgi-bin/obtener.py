# Obtene el valor de todas las respuestas en un form a menos que sean archivos.
# Si no hay respuesta, se guarda un "".
def obtenerRespuestas(form, campos):
    ans = []
    for campo in campos:
        if campo in form:
            # Si tiene filename, significa que subio un archivo.
            if form[campo].filename:
                ans += [form[campo]]
            # Si es un archivo vacio
            elif form[campo].value == b"":
                ans += [""]
            #Si es un string cualquiera
            else:
                ans += [form[campo].value]
        else:
            ans += [""]
    return ans

# Obtiene el id de un valor especifico de una columna especifica en una tabla especifica
def obtenerID(valor, columna, tabla, db):
    sql = f"SELECT id FROM {tabla} WHERE {columna}='{valor}'"
    return db.obtener_data(sql)[0][0]

# Obtiene el país a partir del id de la ciudad
def obtenerPais(id, db):
    sql = "SELECT pais.nombre FROM pais JOIN ciudad ON pais.id=ciudad.pais WHERE ciudad.id=%s;"
    return db.obtener_data(sql, [id])[0][0]

# Obtiene la ciudad a partir de su id
def obtenerCiudad(id, db):
    sql = "SELECT nombre FROM ciudad WHERE id=%s;"
    return db.obtener_data(sql, [id])[0][0]

def obtenerKilos(id, db):
    sql = "SELECT valor FROM kilos_encargo WHERE id=%s;"
    return db.obtener_data(sql, [id])[0][0]

def obtenerEspacio(id, db):
    sql = "SELECT valor FROM espacio_encargo WHERE id=%s;"
    return db.obtener_data(sql, [id])[0][0]

def obtenerViaje(id, db):
    sql = "SELECT * FROM viaje WHERE id=%s"
    return db.obtener_data(sql, [id])[0] 

#Obtiene una lista de viajes de largo "cantidad" desde una fila "desde" específica.
def obtenerListaViajes(desde, cantidad, db):
    sql = f'''SELECT * FROM viaje ORDER BY id ASC LIMIT {desde}, {cantidad}'''
    return db.obtener_data(sql, id) 

def obtenerEncargo(id, db):
    sql = "SELECT * FROM encargo WHERE id=%s"
    return db.obtener_data(sql, [id])[0] 

#Obtiene una lista de encargos de largo "cantidad" desde una fila "desde" específica.
def obtenerListaEncargos(desde, cantidad, db):
    sql = f'''SELECT * FROM encargo ORDER BY id ASC LIMIT {desde}, {cantidad}'''
    return db.obtener_data(sql) 



# Respuestas corresponde a la lista de respuestas rescatadas del form
def obtenerRespuestasSQLViaje(respuestas, db):
    respuestasSQL=[]
    respuestasSQL += [obtenerID(respuestas[1], "nombre", "ciudad", db)]
    respuestasSQL += [obtenerID(respuestas[3], "nombre", "ciudad", db)]
    respuestasSQL += [respuestas[4], respuestas[5]]
    respuestasSQL += [obtenerID(respuestas[7], "valor", "kilos_encargo", db)]
    respuestasSQL += [obtenerID(respuestas[6], "valor", "espacio_encargo", db)]
    respuestasSQL += [respuestas[8], respuestas[9]]
    return respuestasSQL


# Respuestas corresponde a la lista de respuestas rescatadas del form
def obtenerRespuestasSQLEncargo(respuestas, db):
    respuestasSQL=[]
    respuestasSQL += [respuestas[0]] #Descripción
    respuestasSQL += [obtenerID(respuestas[1], "valor", "espacio_encargo", db)]
    respuestasSQL += [obtenerID(respuestas[2], "valor", "kilos_encargo", db)]
    respuestasSQL += [obtenerID(respuestas[4], "nombre", "ciudad", db)]
    respuestasSQL += [obtenerID(respuestas[6], "nombre", "ciudad", db)]
    respuestasSQL += [respuestas[10], respuestas[11]] #email y celular
    respuestasSQL += [respuestas[7], respuestas[8], respuestas[9]] #fotos al final
    return respuestasSQL


# Obtiene la información referente a un viaje usando como parámetro una row de la tabla viajes.
def obtenerInformacionViaje(sqlRes, db):
    ans = [obtenerPais(sqlRes[1], db), obtenerCiudad(sqlRes[1], db), obtenerPais(sqlRes[2], db), obtenerCiudad(sqlRes[2], db),
            str(sqlRes[3])[:10], str(sqlRes[4])[:10], obtenerEspacio(sqlRes[6], db), obtenerKilos(sqlRes[5], db), sqlRes[7], sqlRes[8]]
    return ans

#Obtiene la lista de fotos disponibles a partir de la id de un encargo
def obtenerListaFotos(id, db):
    sql = f'''SELECT ruta_archivo FROM foto WHERE {id}=encargo_id ORDER BY id ASC'''
    return db.obtener_data(sql) 

# Obtiene la información referente a un encargo usando como parámetro una row de la tabla encargos.
def obtenerInformacionEncargo(sqlRes, db):
    fotos = obtenerListaFotos(sqlRes[0], db)
    sources = []
    for foto in fotos:
        sources += [f"src='../media/{foto[0]}'"] 

    # comentario, espacio, kilos, pais origen, ciudad origen, pais destino, ciudad destino, correo, telefono
    ans = [sqlRes[1], obtenerEspacio(sqlRes[2], db), obtenerKilos(sqlRes[3], db), obtenerPais(sqlRes[4], db), obtenerCiudad(sqlRes[4], db),
            obtenerPais(sqlRes[5], db), obtenerCiudad(sqlRes[5], db), sqlRes[6], sqlRes[7]] + sources
  
    return ans  #primeras 8 corresponden a info del encargo, ultimas 3 al source de las 3 fotos

