def calcular_media(numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    return media

numeros = [60, 70, 80, 90, 100]

resultado = calcular_media(numeros)

print("La media de los numeros es:", resultado)
