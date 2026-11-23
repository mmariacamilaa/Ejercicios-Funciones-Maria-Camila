def obtener_impares(numeros):
    impares = []

    for numero in numeros:
        if numero % 2 != 0:
            impares.append(numero)

    return impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultado = obtener_impares(numeros)

print("Los numeros impares son:", resultado)
