import requests


def enviar_mensaje():
    
    datos = {
        "name": "Juan Perez",
        "email": "jperez@email.com",
        "message": "Mensaje de Prueba"
    }

    response = requests.post("http://localhost:8880/form", data=datos)

    print(response.text)

    if "Mensaje enviado" in response.text:
        print("El formulario fue enviado!")
    else:
        print("Ocurrió un errror!!!")


enviar_mensaje()