
def es_bisiestro(year):

    if year % 4 != 0:
        return("no es bisiestro")
    elif year % 4 == 0:
        return("Es bisiestro")
    else:
        return("ERROR")



year = es_bisiestro(2021)

print(year)




