# 1 - Imports
import random;

# 2 - Definição de Funções:
def gerar_nota_aleatoria():
    # Retorna um número flutuante arredondado com 1 casa decimal
    return round(random.uniform(0.0, 10.0), 1)

def verificar_situacao(nota)
    if nota >= 6.0:
        return "Aprovado"
    else: 
        return "Reprovado"

# 3. Código Principal
nota_aluno = gerar_nota_aleatoria()
situacao = verificar_situacao(nota_aluno)

print(f"Nota gerada: {nota_aluno}")
print(f"Situação do aluno: {situacao}")