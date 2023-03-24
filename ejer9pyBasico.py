# Pedimos al usuario una lista de países separados por comas
paises_input = input("Introduce una lista de países separados por comas: ")

# Convertimos la entrada del usuario en una lista
paises = paises_input.split(",")

# Eliminamos los posibles espacios en blanco que puedan haber quedado
paises = [pais.strip() for pais in paises]

# Eliminamos los posibles países repetidos haciendo uso de un set
paises = list(set(paises))

# Ordenamos la lista de países alfabéticamente
paises.sort()

# Mostramos por consola la lista de países separados por comas
print(",".join(paises))

