from calculadora.calculadora import sumar, restar, multiplicar, dividir

a = 10
b = 5

resultado_suma = sumar(a, b)
resultado_resta = restar(a, b)
resultado_multiplicacion = multiplicar(a, b)
resultado_division = dividir(a, b)

print("La suma de", a, "y", b, "es:", resultado_suma)
print("La resta de", a, "y", b, "es:", resultado_resta)
print("La multiplicación de", a, "y", b, "es:", resultado_multiplicacion)
print("La división de", a, "y", b, "es:", resultado_division)