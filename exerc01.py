#---------------------------------------------------------------------------------------------------------------------------
# Escreva um programa que solicite ao usuário um número decimal positivo. O programa deve calcular e exibir na tela:
# A raiz quadrada do número digitado;
# O valor arredondado para cima (utilizando a função adequada do módulo math );
# O valor arredondado para baixo (utilizando a função adequada do módulo math ).
#--------------------------------------------------------------------------------------------------------------------------


import math

numero = float(input("Digite um número decimal positivo: "))

raiz_quadrada = math.hypot(numero, 0)
valor_cima = math.ceil(numero)
valor_baixo = math.floor(numero)

print(f"Raiz quadrada: {raiz_quadrada}")
print(f"Arredondado para cima: {valor_cima}")
print(f"Arredondado para baixo: {valor_baixo}")

