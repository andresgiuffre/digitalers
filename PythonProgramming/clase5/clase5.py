# Servicios Web

# JSON (JavaScript Object Notation)
"""
{
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Ciudad de Ejemplo"
    "casado": false,
    "hobbies": ["lectura", "ciclismo", "jardinería"]
}
"""

# Conexión al Servicio Web

# REpresentational State Transfer (REST)

# Una petición la formamos de esta manera:

# 1) Un verbo HTTP que va a definir la operación que queremos realizar
# 2) Una cabecera (header) que incluye información sobre la petición
# 3) Una ruta (path) hacia un recurso
# 4) Un cuerpo de mensaje (body) con los datos de la petición

# http://api.instituodemo.com/

# Los recursos de esta aplicación serían:

# /alumno, /instructor, /administrativo

# Verbos HTTP (métodos):
# 
# 1) GET - se usa para leer información
# 2) POST - se usa para agregar información nueva
# 3) PUT - se usa para modificar información que ya existe
# 4) DELETE - se usa para eliminar información

# GET /alumno --> Obtiene listado de alumnos
# POST /alumno --> Agrega un nuevo alumno
# DELETE /alumno/3 --> Elimina al alumno con número identificador 3
# PUT /alumno/4 --> Modifica el alumno con número identificador 4
# GET /alumno/5 --> Trae información del alumno número 5

# Para usar esto es Python instalamos el módulo requests (pip install requests)

import requests

#response = requests.get("https://google.com/")
#print(response.status_code)

# Códigos de Estado

"""
- 200 OK - Indica que la solicitud fue exitosa

- 201 Created - Indica que la solicitud fue exitosa y se creó un nuevo recurso

- 204 No Content - La solicitud fue exitosa, pero no hay contenido para devolver

- 400 Bad Request - La solicitud que envía el cliente es incorrecta o mal formada

- 401 Unauthorized - El cliente no está autorizado para acceder al recurso. Puede que requiera
                    autenticación

- 403 Forbidden - El cliente no tiene permisos para acceder al recurso

- 404 Not Found - El recurso solicitado no se encuentra en el servidor

- 500 Internal Server Error - Son problemas del lado del servidor, posiblemente código erróneo.

- 503 Service Unavailable - El servidor no está disponible temporalmente
"""

response = requests.get("https://api.github.com/events")
print(response.json()) # json() nos convierte la devolución del servidor en datos que python maneje
print(response.status_code)

# Instalo módulo para crearme un servicio de prueba (pip install flask)

