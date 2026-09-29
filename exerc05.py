# 1. Imports
import math


# 2. Funções
def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
    return hipotenusa


# 3. Código Principal
cateto_a = float(input("Digite o valor do cateto A: "))
cateto_b = float(input("Digite o valor do cateto B: "))

resultado = calcular_hipotenusa(cateto_a, cateto_b)

print("A hipotenusa é:", resultado)