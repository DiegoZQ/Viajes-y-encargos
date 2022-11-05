import hashlib
import mysql.connector

# Clase encarga de hacer la conexión con mysql
class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    # Verifica que se puede hacer una modificación en la base de datos
    def modificar_data(self, sql, data):
        try:
            self.cursor.execute(sql, data)  # ejecuto la consulta
            return 1 # éxito
        except:
            return 0 # fracaso

    def obtener_data(self, sql, data=None):
        self.cursor.execute(sql, data)
        return self.cursor.fetchall()

    def agregar_viaje(self, data):
        sql = '''
              INSERT INTO viaje (origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
              ''' 
        success =  self.modificar_data(sql, data)
        if success:
            self.db.commit() # modifico la base de datos
        return success

    def agregar_encargo(self, data):
        encargo = data[:7]
        fotos_data = data[7:]
        fotos = []
        for foto in fotos_data:
            if foto != "":
                fotos += [foto]

        sql = '''
              INSERT INTO encargo (descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador)
              VALUES (%s, %s, %s, %s, %s, %s, %s)
              '''
        sql_file = '''
                INSERT INTO foto (ruta_archivo, nombre_archivo, encargo_id) 
                VALUES (%s, %s, %s)
                '''
        hash_names = []

        # Si no es posible agregar el encargo en la tabla de encargos retorna 0.
        if not self.modificar_data(sql, encargo):
            return 0

        # Es necesario subir la row a la tabla encargo para que después poder ver si puedo agregar la llave foránea a la tabla  de foto
        self.db.commit() 

        # Obtiene los índices ficticios actuales que deberia tener la foto y el encargo que vamos a insertar a continuación

        # Obtengo el índice de la orden que acabo de insertar.
        actual_order_index = self.obtener_data("SELECT id FROM encargo ORDER BY id DESC LIMIT 1")[0][0]

        # Calculo el indice de mi foto actual a partir del indice de la ultima foto insertada. Es 1 si es que no hay foto insertada.
        last_pic_index = self.obtener_data("SELECT id FROM foto ORDER BY id DESC LIMIT 1")
        if len(last_pic_index)==0:
            actual_pic_index = 1
        else:
            actual_pic_index = last_pic_index[0][0] + 1


        success = 1

        # Verifica si es posible insertar las fotos en la tabla de fotos, si elimina el encargo ingresado y retorna 0.
        for foto in fotos:
            hash_name = hashlib.sha256(foto.filename.encode()).hexdigest()[0:30] + f"_{actual_pic_index}" #le asigna un hash_name
            hash_names += [hash_name]
            actual_pic_index += 1
            if not self.modificar_data(sql_file, [hash_name, foto.filename, actual_order_index]):
                success = 0
                break
            
        if not success:
            self.modificar_data("DELETE FROM encargo WHERE id=%s", actual_order_index)
            self.db.commit() 
            return 0
            

        # Si llegamos a este punto, significa que sí es posible agregar el encargo y la foto de forma correcta.
        
        # Guardamos los archivos localmente.
        for i in range(len(fotos)):
            open(f"media/{hash_names[i]}", "wb").write(fotos[i].file.read())

        # Guardamos cambios en la base de datos.
        self.db.commit() 

        # Éxito
        return 1
