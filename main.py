from paquete1 import login
from paquete1.cliente import Cliente

def main():
    print("Bienvenido a X")
    seguirLoop = True

    while seguirLoop:
        try:
            option = int(input("Escriba el numero de la opción a elegir.\n1. Ingresar\n2. Registrar\n3. Salir\n"))

            if option == 1:
                usuario = login.ingresar()

                if usuario:
                    cliente = Cliente(usuario['nombre'], usuario['email'], usuario['edad'], usuario['interes'], usuario['celular'])
                    print(f"Bienvenido {cliente.nombre}")

                    while True:
                        print("\nOpciones de compra:")
                        print("1. Realizar compra")
                        print("2. Mostrar datos del cliente")
                        print("3. Mostrar lista de compras")
                        print("4. Salir")

                        opcion = int(input("Seleccione una opcion: "))

                        if opcion == 1:
                            print("Opciones de objetos:")
                            print("1. Laptop")
                            print("2. Heladera")
                            print("3. Celular")
                            print("4. Microondas")
                            print("5. Televisor")

                            objetoOpcion = int(input("Seleccione un objeto para comprar: "))

                            objetosDisponibles = {
                                1: "Laptop",
                                2: "Heladera",
                                3: "Celular",
                                4: "Microondas",
                                5: "Televisor"
                            }

                            objetoElegido = objetosDisponibles.get(objetoOpcion)

                            if objetoElegido:
                                print("Opciones de lugares:")
                                print("1. Wallmart")
                                print("2. Frabega")
                                print("3. Cetrogar")
                                print("4. Musimundo")
                                print("5. Empresa Generica")

                                lugarOpcion = int(input("Seleccione un lugar para comprar: "))

                                lugaresDisponibles = {
                                    1: "Wallmart",
                                    2: "Frabega",
                                    3: "Cetrogar",
                                    4: "Musimundo",
                                    5: "Empresa Generica"
                                }

                                lugarElegido = lugaresDisponibles.get(lugarOpcion)

                                if lugarElegido:
                                    compra = f"{objetoElegido} en {lugarElegido}"
                                    cliente.añadirObjeto(compra)
                                    print(f"Compra de {compra} realizada con exito.")
                                else:
                                    print("Opcion de lugar invalida")
                            else:
                                print("Opcion de objeto invalida")

                        elif opcion == 2:
                            cliente.mostrarDatos()
                        elif opcion == 3:
                            cliente.show_list()
                        elif opcion == 4:
                            print("Cerrando...")
                            seguirLoop = False  # Salir del bucle principal
                            break  # Salir del bucle interno
                        else:
                            print("Opcion invalida")

            elif option == 2:
                seguirRegistrando = True

                while seguirRegistrando:
                    try:
                        login.crear_cuenta()
                        x = int(input("¿Deseas crear otra cuenta?\n1. Sí\n2. No\n"))

                        if x == 1:
                            seguirRegistrando = True
                        elif x == 2:
                            seguirRegistrando = False
                        else:
                            print("Opción incorrecta.")
                            break

                    except Exception as e:
                        print("Error en registro.")
                        print(f"Error inesperado: {type(e).__name__}")

            elif option == 3:
                print("Cerrando...")
                seguirLoop = False

            else:
                print("Numero invalido.")

        except ValueError:
            print("Debe ingresar un numero.")
        except Exception as e:
            print("Error en ingreso.")
            print(f"Error inesperado: {type(e).__name__}")

if __name__ == "__main__":
    main()
