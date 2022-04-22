class Pollo:
    def __init__(self, nombre, genero, edad) -> None:
        self. nombre = nombre
        self.genero = genero
        self.edad = edad
    

class Pollito(Pollo):
    def __init__(self, nombre, genero, edad, color) -> None:
        super().__init__(nombre, genero, edad)
        self.color = color
kendall = Pollo("Kendall", "Hembra", 2)
# xd
print(kendall.genero)

kendall_super_pollito = Pollito("Kendall", "Hembra", 2, "gris")
print(kendall_super_pollito)

# Archivo de practica POO, Ayudo a comprender el funcionamiento de las clases 
# para implementar una interfaz de usuario.
# se decide dejar mantener en la carpeta en forma de tributo :)