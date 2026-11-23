def calcular_producto(numeros):
    producto = 1

    for numero in numeros:
        producto = producto * numero

    return producto

numeros = [5, 6, 7,8]

resultado = calcular_producto(numeros)

print("El producto de los numeros es:", resultado)
