"""
Condicional -> Estrutura de decisões
No python nós temos o :
if -> Se
elif -> Se não se
else -> se não
"""
# Estrutura
print('Algoritmo para cálculo de média: ')
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(media)  # 39

if media >= 60:  # Falso
    print('Verdadeiro')
    print(f'Aluno aprovado com média {media}')

elif 40 <= media <= 60:  # Falso
    print(f'Aluno de exame final {media}')
else:
    print(f'Aluno reprovado ')



