texto = """
Aula de revisão 1 semestre
1 - Variáveis
2 - Comandos básicos
3 - Operadores aritméticos
4 - Operadores relacionais
5 - If/elif/else
6 - Loops

# Um algoritmo básico contém
Entradas
-inputs

Processamento
-Cálculos

Saída
-prints

1 - Variáveis
- São palavras definidas pelo programador para salvar informações.
nome = "Felipe"
idade = 26
admin = True
horasLogado = 1.5

1.1 - Tipos de valores básicos
string -> Textos  # Strings são definidas por aspas simples ou duplas ( 'string', "string")
int -> números inteiros  # Basta inserir os números, sem caracteres especiais (18)
float -> ponto flutuante  # Números com casas decimais, separado por . "ponto" (18.0)
bool -> Valor booleano # Contém apenas 2 valores, True ou False (verdadeiro ou falso)

2 - Comandos básicos
-Comando escrever (print)
print -> Escreve uma mensagem no console 

Exemplos: 
print("Olá, Mundo!")  # Podemos escrever textos diretos
print(nome)  # Podemos escrever variáveis
print(f"Olá, {nome}!")  # Podemos escrever textos e variáveis juntos
Obs: Para isso utilizamos a letra f no começo da entrada do print, esse f significa format
     colocamos a variável dentro de chaves {}

- Comando ler (input)
input -> Lê uma entrada de dados do usuário no console
Obs: É necessário salvar o valor em uma variável

Exemplos

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))

Obs1: Por padrão o valor é uma string, para converter o valor, colocamos antes do input 
o tipo de valor que queremos

3 - Operadores aritméticos

# Operadores aritméticos são basicamente utilizados para efetuar cálculos matemáticos
São eles:
+  -> Soma
-  -> Subtração
/  -> Divisão
*  -> Multiplicação
** -> Potência
=  -> Atribuição de valor
() -> Definir a prioridade
// -> Divisão (retorna apenas o valor do inteiro)

Exemplos
print(14+3)  # 17 
print(14-3)  # 11
print(14/3)  # 4.666666...7
print(14//3) # 4
print(14*3)  # 42
print(14**3) # 2744
print(14+3/2) # 15.5
print((14+3)/2) # 8.5

4 - Operadores relacionais
#  Os operadores relacionais diferentemente dos aritméticos NÃO mudam os valores envolvidos
#  Servem basicamente para comparações, assim sendo, retornando apenas Verdadeiro ou Falso
São eles:

>  -> Maior
<  -> Menor
== -> É igual
>= -> Maior ou igual
<= -> Menor ou igual
!= -> Diferente
and -> E
or  -> Ou
not -> Negação

Exemplos: 
print(4 > 3)  # True
print(4 < 3)  # False
print(4 >= 3)  # True
print(4 <= 3)  # False
print(4 == 3)  # False
print(4 != 3)  # True

# Comparando variáveis
x = 4
y = 4.0

print(y+x)
print(y==x)

5 - if/elif/else  # Condicionais (Se, senão se, senão)
# Utilizamos condicionais quando queremos tomar uma decisão com base em uma resposta verdadeira ou falsa
# Chamamos essa estrutura de bloco de decisão, ela obrigatoriamente inicia com o IF (SE)

nome = "Bátima da Silva"
idade = 30
admin = False


# Descobrindo se o usuário é admin
if admin == True: # ------- Início do bloco IF--------
    print("Todos os comandos estão liberados")
else:
    print("Alguns comandos estão bloqueados porque você não é admin")
# ----- Fim do bloco IF -------

# Descobrindo se o usuário é maior de idade
if idade >= 18: # ----- Início do bloco IF ------
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
# ------ Fim do bloco if ------
"""

nome = "Bátima da Silva"
idade = 14
admin = False


if admin == True and idade >= 18:
    print("Você é admin e tem mais de 18 anos.")
elif admin == True and idade < 18:
    print("Você é admin mas tem menos de 18 anos. ")
elif admin == False and idade >= 18:
    print("Você é maior de idade, mas não é admin.")
else:
    print("Você é menor de idade e não é admin.")
