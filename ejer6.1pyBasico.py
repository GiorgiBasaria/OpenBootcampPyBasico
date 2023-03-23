
class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas



class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


mi_coche = Coche("Gris", 4, 5, 120, 1600)
print("Mi coche es de color ", mi_coche.color)
print("Mi coche tiene", mi_coche.ruedas, "ruedas")
print("Tiene", mi_coche.puertas, "puertas")
print("Va una velocidad de ", mi_coche.velocidad, "km/h")
print("Tiene una cilindrada de ", mi_coche.cilindrada, "cc")