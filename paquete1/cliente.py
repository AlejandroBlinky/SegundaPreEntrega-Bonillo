class Cliente:
    def __init__(self, nombre, email, edad, interes, celular):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.interes = interes
        self.celular = celular
        self.objetosComprados = []

    def mostrarDatos(self):
        print(f"Datos del cliente:")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Edad: {self.edad}")
        print(f"Interes: {self.interes}")
        print(f"Numero de celular: {self.celular}")

    def añadirObjeto(self, objeto):
        self.objetosComprados.append(objeto)
        print(f"El objeto '{objeto}' se agrego a la lista de compras de {self.nombre}.")

    def show_list(self):
        print(f"Lista actual de objetos:")
        for objeto in self.objetosComprados:
            print(objeto)

    def __str__(self):
        return self.nombre

        