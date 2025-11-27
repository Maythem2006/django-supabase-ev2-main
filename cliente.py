import requests
import time


BASE_URL = "http://127.0.0.1:8000"
TOKEN_URL = "/api/token/"
REFRESH_URL = "/api/token/refresh/"
RESOURCE_ENDPOINT = "/api/Contacto/" # cámbialo según tu API


def main():
    print("CLIENTE API JWT")
    user = input("Usuario: ")
    pw = input("Clave: ")

    token = requests.post(BASE_URL + TOKEN_URL, data={"username": user, "password": pw})
    print("Status:", token.status_code)
    
    if token.status_code != 200:
        print(f"Error de autenticación: {token.status_code}")
        print(token.text)
        return

    print("\n1) Listar\n2) Crear\n")
    op = input("Elige opción: ")

    if op == "1":
        access_token = token.json().get("access")
        headers = {"Authorization": f"Bearer {access_token}"}

        r = requests.get(BASE_URL + RESOURCE_ENDPOINT, headers=headers)
        print("Status:", r.status_code)
        
        if r.status_code == 200:
            print(r.json())
        elif r.status_code == 404:
            print("Error 404: Recurso no encontrado")
        elif r.status_code == 401:
            print("Error 401: No autorizado")
        elif r.status_code == 500:
            print("Error 500: Error interno del servidor")
        else:
            print(f"Error {r.status_code}: {r.text}")

    elif op == "2":
        access_token = token.json().get("access")
        headers = {"Authorization": f"Bearer {access_token}"}

        nombre = input("Nombre: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")
        direccion = input("Direccion: ")
        

        data = {"nombre": nombre, "correo": correo, "telefono": telefono, "direccion": direccion}
        r = requests.post(BASE_URL + RESOURCE_ENDPOINT, headers=headers, data=data)
        print("Status:", r.status_code)
        
        if r.status_code in [200, 201]:
            print(r.json())
        elif r.status_code == 404:
            print("Error 404: Recurso no encontrado")
        elif r.status_code == 400:
            print("Error 400: Solicitud inválida")
            print(r.json())
        elif r.status_code == 401:
            print("Error 401: No autorizado")
        elif r.status_code == 500:
            print("Error 500: Error interno del servidor")
        else:
            print(f"Error {r.status_code}: {r.text}")

    else:
        print("Opción inválida.")


if __name__ == "__main__":
    main()






