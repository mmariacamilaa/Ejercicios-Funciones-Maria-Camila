def interseccion(lista1, lista2):
    resultado = []

    for elemento in lista1:
        if elemento in lista2 and elemento not in resultado:
            resultado.append(elemento)

    return resultado

print(interseccion([1, 2, 1], [2, 3, 2, 4])) 