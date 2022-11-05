# Tarea 2
Código fuente de una plataforma para enviar encargos, usando el espaico disponible en las 
maletas de de los viajeros voluntarios. Los viajeros voluntarios podrán ingresar al sistema
información de un viaje futuro, informando el origen y el destino, fechas de ida y regreso, junto
con el espacio y kilos dosponibles. Los interesados en realizar encargos, podrán consultar los viajes 
cubiertos por los viajeros voluntarios e ingresar al sistema sus encargos, con origen y destino, descripción
del encargo, foto/s del encargo, y contacto. De la misma forma también se podrá ver la lista de encargos
ingresados al sistema. Todo esto se realizó usando html, css (bootstrap), javascript, una base de datos en MySQL
y python cgi en el puerto 8000.

Para ver la página web en local:

- Correr Apache y MySQL desde XAMPP
- Importar la base de datos tarea2.sql y pais-ciudad.sql
- Correr el comando para servir desde tu localhost: <code>  python -m http.server --bind localhost --cgi 8000</code>.
- Ir a la url en (http://[::1]:8000/cgi-bin/inicio.py), desde el navegador, para visualizar la página.