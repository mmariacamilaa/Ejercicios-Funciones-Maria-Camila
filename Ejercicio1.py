
def perimetro_triangulo(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

resultado = perimetro_triangulo(lado1, lado2, lado3)

print("El perimetro del triangulo es:", resultado)
