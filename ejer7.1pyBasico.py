import time

hora_actual = time.localtime().tm_hour


if hora_actual >= 18:
    print("¡Hora de ir a casa!")
else:
    minutos_restantes = (18 - hora_actual) * 60

    print(f"Aún quedan {minutos_restantes} minutos para ir casa")