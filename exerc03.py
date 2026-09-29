# Escreva uma função chamada encontrar_maior(a, b, c) que receba três números inteiros como
# parâmetros e retorne qual deles é o maior valor.
# No código principal, peça 3 números ao usuário, execute a função criada e exiba na tela o valor
# retornado.

import math

def encontrar_maior(a, b, c):
    return max(a, b, c)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = encontrar_maior(num1, num2, num3)
print(f"O maior valor é: {maior}")