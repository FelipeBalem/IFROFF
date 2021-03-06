"""
Loops - Blocos de repetição
Eles servem para repetir um bloco de código uma quantidade determinada ou
indeterminada de vezes
DETERMINADA - for / para
O for permite que o programador decida quantas vezes o bloco será repetido

INDETERMINADO - while / enquanto
O while permite que o bloco seja repetido quantas vezes forem necessárias até que uma
condição seja satisfeita

# Escreva 10 linhas dizendo 'Olá, Mundo!"
                # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for repeticao in range(10):  # para variável em iterável faça:  # Iterável é todo valor que
    print("Olá, mundo!")  # # pode ser percorrido! listas, ranges, textos
    print(f'repetição = {repeticao}')
print("Agora estou fora do 'for'!")

# Exemplos for

for letra in 'Felipe Balem':  # Para cada elemento dentro de um alcance X
    print(letra)
# Exemplo While - Enquanto
numero = 0
while numero < 10:
    numero = numero + 1
    print(numero)
    # Refatorando o cálculo
escolha = None

while escolha != 'p' and escolha != 'm' and escolha != 'g':
    #escolha = input('Qual valor quer descobrir: (p) Peso, (m) Massa, (g) Gravidade: ')
    escolha = 'g'
    escolha = escolha.lower()  # Forçando o texto a ficar minúsculo.
    if escolha != 'p' and escolha != 'm' and escolha != 'g':
        print("Comando não reconhecido, tente novamente")

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
escolha = None
# Cuidado com loops infinitos quando utilizar o while
# O loop infinito acontece quando a condição do while nunca será satisfeita.

# no caso de um loop infinito no Pycharm você pode pressionar Ctrl + C para parar
while escolha != 'p' and escolha != 'm' and escolha != 'g':
    print(escolha)
numero = 0
while numero <= 10: # Enquanto condição for verdadeira, faça:
    print(numero)
    numero = numero + 1 # numero += 1
print("Agora estou fora do while")
# Faça um algoritmo que faça o cadastro de 5 pessoas, perguntando nome e idade.
for repeticao in range(5):
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    print(f"Seu nome é {nome} e tem {idade} anos. Seu ID é {repeticao+1}")

#Extra for
valor = int(input("Digite o valor máximo pra ver a lista de número ímpares e pares até ele"))
for numero in range(valor):
    print(numero)
    if numero % 2:
        print("Número ímpar")
    else:
        print('Número par')


# Faça um algorimo que faça cadastro de pessoas com nome e idade e só pare quando for
# digitado 'sair' no campo nome.
nome = None
rep = 1
while nome != 'sair': # Enquanto condição for verdadeira, faça:
    nome = input("Digite o seu nome: ")
    if nome == 'sair':
        break  # Break é utilizado para forçar uma saída do while
    idade = input("Digite a sua idade: ")
    print(f" seu nome é {nome} e tem {idade} anos. Seu ID é {rep}.")
    rep += 1
print('sai do while')

# Escreva um algoritmo em Python que imprima na tela a sequência de 1 até 100, 2 vezes.
# Uma vez utilizando for e outra, while.

# FOR
for i in range(100):
    print(i+1)

# while
i = 0
while i <= 100:
    print(i)
    i += 1

# Um algoritmo que recebe um número inteiro (n) e faz a soma de todos os números entre 0 e n

n = int(input("Digite um número: ")) # 10
soma = 0
for numero in range(n):
    print(f"{soma} + {numero}")  # Vendo o que está sendo somado
    soma = soma + numero
    print(f"Soma parcial: {soma}")
print(f"A soma dos valores é: {soma}")

# Um algoritmo que recebe um valor natural n e imprime todos os números naturais até n.

n = int(input("Digite um número: "))
for numero in range(n):
    print(numero)

# Um algoritmo que receba um quantidade de números naturais e informe qual deles é o maior,
# o algoritmo só para de receber números quando o número 0 for digitado.

# Um algoritmo que receba um quantidade de números naturais e informe qual deles é o maior,
# o algoritmo só para de receber números quando o número 0 for digitado.

maior = 1
numero = 1

while numero != 0:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    elif numero > maior:
        maior = numero

print(f"O maior número digitado foi {maior}")


# Extra - Maior e menor
maior = 1
numero = 1
menor = 999
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"O maior número digitado foi {maior}")
print(f"O menor número digitado foi {menor}")
"""

# Um programa que simule o lançamento de 2 dados, n vezes, e tem como saída o
# número de cada dado e a relação ( >, <, == ) entre eles.

# PS: Para esse algoritmo é utilizado uma função que ainda não aprendemos,
# ignore ela por enquanto, foque apenas na função do loop e dos operadores relacionais

from random import randint
n = int(input("Digite quantos lançamentos serão feitos: "))
for lancamento in range(n):
    print(f"Lançamento: {lancamento}")
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    print(f"Dado 1 = {dado1}")
    print(f"Dado 2 = {dado2}")
    if dado1 > dado2:
        print("Dado 1 > Dado 2")
    elif dado2 > dado1:
        print("Dado 2 > Dado 1")
    else:
        print("Os dois dados são iguais")


