import json
import os

def ingresar():
    print("Ingrese sus datos de cuenta.")
    usuario = input("usuario: ")
    pw = input("Contrasenia: ")
    
    if usuario and pw:
        if not os.path.isfile("./datos.json"):
            print("No se encontro el archivo de datos.")
            return

        with open("./datos.json", "r") as file:
            dataRead = json.load(file)

        for user in dataRead.get("usuario", []):
            if user['usuario'] == usuario and user['contrasenia'] == pw:
                print(f"Bienvenido {user['nombre']}")
                return user

        print("Usuario o contrasenia incorrectos.")
    else:
        print("Por favor, rellene todos los campos requeridos.")
        return ingresar()

def validar_info(usuario, pw, nombre, email, edad, interes, celular):
    return all([usuario, pw, nombre, email, edad, interes, celular])

def crear_cuenta():
    print("Registra tu nueva cuenta.")
    usuario = input("usuario: ")
    pw = input("Contrasenia: ")
    nombre = input("Nombre: ")
    email = input("Email:")
    edad = int(input("Edad: "))
    interes = input("Un interes: ")
    celular = int(input("Celular: "))

    if validar_info(usuario, pw, nombre, email, edad, interes, celular):
        data = {
            'usuario': [{
                'usuario': usuario,
                'contrasenia': pw,
                'nombre': nombre,
                'email': email,
                'edad': edad,
                'interes': interes,
                'celular': celular,
            }]
        }

        if not os.path.isfile("./datos.json"):
            with open("./datos.json", "w") as file:
                json.dump(data, file, indent=4)
                print("Archivo de datos creado.")
        else:
            with open("./datos.json", "r") as file:
                dataRead = json.load(file)

            if dataRead.get("usuario"):
                for user in dataRead["usuario"]:
                    if user['usuario'] == usuario:
                        print("Ese nombre de usuario ya esta en uso.")
                        return

                dataRead["usuario"].append(data['usuario'][0])
                with open("./datos.json", "w") as file:
                    json.dump(dataRead, file, indent=4)
                    print("Cuenta creada exitosamente!")
            else:
                with open("./datos.json", "w") as file:
                    json.dump(data, file, indent=4)
                    print("Cuenta creada exitosamente!")
    else:
        print("Por favor, rellene todos los campos requeridos.")
