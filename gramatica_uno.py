def es_capicua(cadena):
    return cadena == cadena[::-1]

with open("g1_texto.txt", "r") as f:
    cadena = f.read()

if es_capicua(cadena):
    print("La cadena es capicua.")
else:
    print("La cadena no es capicua.")