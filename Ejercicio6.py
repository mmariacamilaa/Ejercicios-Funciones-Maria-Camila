def minimo_maximo(numeros):
    minimo = min(numeros)
    maximo = max(numeros)

    return minimo, maximo

numeros = [30, 4, 45, 2, 39, 15]

menor, mayor = minimo_maximo(numeros)

print("El numero minimo es:", menor)
print("El numero maximo es:", mayor)
