"""
Revisão IF ELSE

IF - SE
ELSE - SE NÃO
ELIF - SE NÃO SE

# IF / ELIF /ELSE - Juntos formas a estrutura de condição no Python para tomada de decisão
Traduzindo a estrutura
------------
SE algo for verdadeiro, faça isso:
    comandos
    comandos
Se não faça aquilo:
    comandos
    comandos
------------
"""

# Exemplo:
# Desenvolva um algoritmo que receba a média de um aluno (0 - 100) e informe se ele está aprovado
# ou reprovado, a média para aprovação é 60
media = float(input('Digite a sua média: '))
if media > 60:  # Se for verdadeiro
    print(f"Você está aprovado média acima de 60: {media}")
elif media == 60:
    print("Passou na rapa em amigão")
else:
    print(f"Você está reprovado com a média {media}")
valor1,valor2 = 10, 8
if valor1 > valor2:
    #  Comando
else:
    # Comando