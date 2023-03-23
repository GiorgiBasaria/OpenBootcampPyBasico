import pickle


# Crear un objeto de la clase Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color


# Crear un objeto de la clase Vehículo
mi_coche = Vehiculo("Ford", "Mustang", "Rojo")

# Guardar el objeto en un archivo con el módulo pickle
with open("mi_coche.pickle", "wb") as archivo:
    pickle.dump(mi_coche, archivo)

# Cargar el objeto del archivo
with open("mi_coche.pickle", "rb") as archivo:
    mi_coche_cargado = pickle.load(archivo)

# Imprimir los atributos del objeto cargado
print("Marca:", mi_coche_cargado.marca)
print("Modelo:", mi_coche_cargado.modelo)
print("Color:", mi_coche_cargado.color)
