"""
print("Texto que deve aparecer em várias \n linhas sem utilizar vários prints")
"""
# \n Quebra de linha
"""
  FÓRMULA POTÊNCIA MÉDIA Pm = F * vm
  Pm = Potência média
  F = força
  Vm = Velocidade Média
  Para descobrir o valor da potência média
"""
"""
#ENTRADA DE DADOS

F = float(input(f"Qual é o valor da força? "))
Vm = float(input(f"Qual é o valor da Velocidade média? "))

# PROCESSAMENTO

Pm = F * Vm

# Saída de dados

print(f"A Potência Média é : {Pm}")
# Forma 1 para descobrir qual valor o usuário quer calcular.
# p = m * g
p = input("Digite o valor do peso \n (digite 'x' ou deixe em branco se não tiver o valor): ")
m = input("Digite o valor da massa \n (digite 'x' ou deixe em branco se não tiver o valor): ")
g = input("Digite o valor da gravidade \n (digite 'x' ou deixe em branco se não tiver o valor): ")
print(type(p))
if not p or p == 'x':
    p = float(m) * float(g)
    print(f'valor de p: {p}')

elif not m or m == 'x':
    m = float(p) / float(g)
    print(f'valor de m: {m}')
else:
    g = float(p) / float(m)
    print(f'valor de g: {g}')

#def pmg(escolha):
"""

# Forma 2
print("Bem vindo ao Física Fácil - Projeto de algoritmos do segundo ano.")
print("Esse algoritmo é para trabalhar com fórmula / função P = M * G")
ajuda = input("Digite 'help' para ver o conceito desta função. Ou tecle Enter para continuar. \n")
ajuda = ajuda.lower()
if ajuda == 'help':
    print("""Peso: 
O Peso (P) é uma grandeza vetorial visto que apresenta intensidade,
 direção e sentido, sendo o produto da massa de um corpo e a aceleração
 da gravidade exercida sobre ele.

    Dessa forma, diferentemente da massa, o peso é um valor variável.
No Sistema Internacional (SI), a unidade padrão do Peso é representada em Newton (N)\n""")

escolha = input('Qual valor quer descobrir: (p) Peso, (m) Massa, (g) Gravidade: ')

escolha = escolha.lower() # Forçando o texto a ficar minúsculo.
if escolha == 'p':  # Escolhendo peso
    print('Ok, vamos descobrir o valor do peso. ')  # Feedback
    massa = float(input('Digite o valor da massa em KG: '))  #  Recebendo os outros valores
    gravidade = float(input('Digite o valor da gravidade em m/s²: '))
    p = massa * gravidade
    print(f"O peso é: {p} N")

elif escolha == 'm':
    print('Ok, vamos descobrir o valor da massa.')
    peso = float(input("Digite o valor do peso em Newton: "))
    gravidade = float(input("Digite o valor da gravidade em m/s²: "))
    m = peso / gravidade
    print(f'O valor da massa é: {m} Kg')

elif escolha == 'g':
    print('Ok, vamos descobrir o valor da gravidade.')
    peso = float(input("Digite o valor do peso em Newton: "))
    massa = float(input("Digite o valor da massa em Kg: "))
    g = peso / massa
    print(f'O valor da massa é: {g} N')

else:
    print('Comando não reconhecido')
# Portas Lógicas

#not - Não - Negação, inverte um valor booleano
#or - Ou - Se uma ou mais entradas forem verdadeiras, a saída será verdadeira
#and - E - TODAS as entradas devem ser verdadeiras para que a saída seja verdadeira

#             OU + OR
# Entradas     | Saída
#   1     1    | 1
#   1     0    | 1
#   0     1    | 1
#   0     0    | 0

#            E * AND
# Entradas    | Saída
#   1     1   | 1
#   1     0   | 0
#   0     1   | 0
#   0     0   | 0

#       NÃO / NOT
#  Entrada    | Saída
#     V       |  F
#     F       |  V