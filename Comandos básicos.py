"""
Comentários:
- Os comentários são blocos de texto que NÃO serão processados
na aplicação, ou seja, apenas o programador consegue vê-los.
- Formas de fazer um comentário:
1) Utilizando TRÊS ASPAS DUPLAS OU SIMPLES """ ''''''
"""
2) Utilizando #
# Obs: O # produz comentários de UMA linha
# Isso é um comentário

# variáveis
# As variáveis são criadas para armazenar uma informação na
# memória do computador

# As mais comuns são:
# Inteiro (int) -> 10, 12, 0, -4, -1000, etc (números inteiros, positivos ou negativos)
# Reais (float) -> 10, 12, 0, -4, -25.6, 67.908765, etc (números reais, que podem 
    conter casas decimais, deve ser usado o ponto ( . ) para separar as casas decimais)
# Texto (str) -> "f" "Felipe", "12", "Felipe 12" (Pode ser textou e/ou números, entretanto
    números inseridos em variáveis do tipo string não conseguem fazer parte de cálculos.
    Strings devem ser colocadas dentro de aspas simples ou duplas
# Booleano (bool) -> True, False (Verdadeiro ou Falso)
                     
Para criar uma variável, a gente tem que criar um identificador
e dar um valor (opcional);
O identificador nada mais é do que um nome para essa variável
Exemplos: 
situacao = "Aluno reprovado" # cria uma variável que recebe uma string
idade = 18 # cria uma variável que recebe um número inteiro

# Comando input
# Esse comando recebe dados do usuário
# Obs: Por padrão o input recebe valores em string (texto)

# Esse código grava o nome
nome = input('Digite o seu nome: ')
print(f) 

# Esse código grava a idade
idade = int(input("Digite a sua idade: ")) #Note que o 'int' presente no código converte
    o valor recebido pelo input em inteiro.

# Comando print

# Esse comando escreve mensagens pro usuário (saída de dados)

# A partir da versão 3.6 utilizamos a letra 'f' no começo
# do texto para formatá-lo
# para adicionar variáveis no texto, insira o nome da variável
# entre chaves {}
print(f"Seu 'nome' é: {nome} e tem {idade} anos.") # Obs: Se não colocar o 'f', o print
    não consegue mudar a variável {nome} para seu respectivo valor.

# PRATICANDO

# Crie um algoritmo que receba 2 valores inteiros e faça
# as 4 operações básicas (soma, subtração, multiplicação
# e divisão) e mostre o resultado para o usuário.

#Entrada de dados (pegando valores com o usuário)
nome = input("Digite o seu nome: ")
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

#Processamento (fazendo os cálculos)
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

#Saída de dados (mostrando a resposta pro usuário)
print(f"Bem vindo {nome}")
print(f"O valor da soma é: {soma}")
print(f"O valor da subtração de {num1} e {num2} é: {sub}")
print(f"O valor da multiplicação dos dois números é: {mult}")
print(f"{num1} / {num2} = {div}")


# Crie um algoritmo que receba o nome de uma pessoa, o ano de
# nascimento, o ano atual e informe qual a idade dessa pessoa.

print("Algoritmo para calcular idade!")  # Mensagem de boas vindas
# Entrada de informação
nome = input("Digite o seu nome: ")  # Recebendo o nome
nome = nome.title()  # Deixar o nome com as primeiras letras maiúsculas
print(f"Bem vindo(a) {nome}!")  # Mensagem de boas vindas com nome
anoNascimento = int(input("Digite o ano que você nasceu: "))
anoAtual = int(input("Digite o ano atual: "))

# Processamento
idade = anoAtual - anoNascimento  # Calculando a idade

# Saída de Informação
print(f"{nome} neste ano você terá {idade} anos completos.")

"""
idade = input("Digite a sua idade: ")
nome = "Felipe"
print(f"Seu 'nome' é: {nome} e tem {idade} anos.")
print("Escreva alguma coisa; ")  # Comentário