def nombres_por_letra(lista, letra):
    resultado = []

    for nombre in lista:
        if nombre.startswith(letra):
            resultado.append(nombre)

    return resultado

nombres = ["Andrea", "Paula", "Ana", "Carolina", "Aurora"]
print(nombres_por_letra(nombres, "A"))