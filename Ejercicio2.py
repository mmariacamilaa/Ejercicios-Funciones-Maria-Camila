def area_circulo(radio):
    pi = 3.1416
    area = pi * radio ** 2
    return area

radio = float(input("Ingrese el radio del circulo: "))

resultado = area_circulo(radio)

print("El area del circulo es:", resultado)
