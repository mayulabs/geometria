import math


def area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        return "Valor de entrada invalido"

    area = (base * altura) / 2
    return float(f"{area:.2f}".rstrip("0").rstrip("."))


def area_triangulo_equilatero(lado):
    if lado <= 0:
        return "Digite um lado valido"

    area = (math.sqrt(3) / 4) * lado * lado
    return float(f"{area:.2f}".rstrip("0").rstrip("."))


def perimetro(lados):
    if any(lado <= 0 for lado in lados):
        return "Lista contém um lado menor ou igual a 0"
    return sum(lados)


def heron(ladoA, ladoB, ladoC):
    if not condicao_existencia_triangulo(ladoA, ladoB, ladoC):
        return "Digite um triângulo válido"

    s = (ladoA + ladoB + ladoC) / 2
    return float(math.sqrt(s * (s - ladoA) * (s - ladoB) * (s - ladoC)))


def condicao_existencia_triangulo(ladoA, ladoB, ladoC):
    return all(
        [
            ladoA > 0,
            ladoB > 0,
            ladoC > 0,
            ladoA + ladoB > ladoC,
            ladoA + ladoC > ladoB,
            ladoB + ladoC > ladoA,
        ]
    )

# TODO Adicionar o cálculo do tipo de triângulo (equilátero, isósceles, escaleno)

