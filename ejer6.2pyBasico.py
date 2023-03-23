class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


    def imprimir(self):
        print("El alumno", self.nombre, "tiene una nota de", self.nota)

    def resultado(self):
        if self.nota >= 5:
            print("El alumno", self.nombre, "ha aprobado.")
        else:
            print("El alumno", self.nombre, "ha suspendido.")

print("-------------------------------")

alumno1 = Alumno("Juan", 8)
alumno1.imprimir()
alumno1.resultado()

print("-------------------------------")

alumno2 = Alumno("Pepe", 4)
alumno2.imprimir()
alumno2.resultado()