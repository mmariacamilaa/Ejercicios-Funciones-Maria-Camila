def cadena_mas_larga(lista):
    mayor = lista[0]

    for cadena in lista:
        if len(cadena) > len(mayor):
            mayor = cadena

    return mayor

# Prueba
nombres = ["Cristian", "Samuel", "David", "Manuel"]
print(cadena_mas_larga(nombres))