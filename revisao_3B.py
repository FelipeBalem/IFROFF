"""
Revisão 3 Bimestre

Variáveis
    - São palavras criadas pelo usuário que direcionam para o seu conteúdo na memória
    Os principais tipos são:
    Inteiro (int): Armazena valores inteiros - ..., -2, -1, 0, 1, 2, .... +
    Ponto Flutuante (float): Armazena valores decimais (conjunto dos números reais):
        - 10.123455...., -9.12321, -1.0, 0.0, 0.1, 0.2, 1.0, 1.2, .... +
    Texto/string (str): Armazena valores textuais: 'isso é uma string'
    # OBS: String SEMPRE devem estar entre aspas simples ou duplas
    Boolean (bool): Armazena valores boelanos (verdadeiro ou falso/ True or False)
    Listas (arrays): Armazena diversos valores em uma lista ['Felipe', 1, 2.2, True, [0, 1, 3]]

    OBS: Variáveis SEMPRE devem ser minúsculas e não podem conter caracteres especiais ou acentuação.
        Também não podem INICIAR com números, mas podemos ter números no meio ou no fim do nome da variável

    POR QUE UTILIZAMOS VARIÁVEIS
    # Porque é muito mais fácil gravar nomes do que endereços de memória, então quando chamamos
    uma variável que foi criada anteriormente, apenas precisamos escrever seu nome, a própria IDE
    irá localizar o valor na memória


nome = 'Felipe'
idade = 26
altura = 1.80
               # 0             1           2                   3
endereco = ['Rua Ariquemes', 2121, 'Setor das andorinhas', 'Ariquemes']
vacinado = True

print(nome)
print(type(nome))
print(idade)
print(type(idade))
print(altura)
print(type(altura))
print(endereco)
print(type(endereco))
print(endereco[0])
print(type(endereco[0]))
print(vacinado)
print(type(vacinado))

Funções

    Funções são ferramentas que utilizamos quando queremos resolver alguma coisa
    Tento um retorno ou não
    Para criar uma função, utilizamos a palavra reservada def
    # Exemplo
    def nome_da_funcao(parâmetros[opcionais]):
        <código da função>
        return resultado

Palavras reservadas (funções do próprio sistema, já vem no Built-ins)
    print() escreve uma mensagem no terminal
    def -> cria uma função
    type -> informa o tipo da variável
    input() recebe uma entrada de dados pelo teclado
Condicionais
    Condicionais são utilizados para tomadas de decisão, basicamente algo como:
    SE <expressão> for verdadeira, faça:
        <comandos>
    se não, faça:
        <outros comandos>

    No python, utilizamos IF (se) ELIF (se não se) e ELSE (se não)
    É obrigatório iniciar com IF, o ELIF e o ELSE são opcionais, o ELSE só pode ser utilizado na ÚLTIMA opcão
    Quando temos IF, ELIF e ELSE no mesmo bloco de código, eles são executados um por vez até que UM
    deles seja verdadeiro, quando o bloco verdadeiro for executado o algoritmo vai PULAR o resto do bloco


nome = 'Felipe'
idade = 70

nome2 = 'Julia'
idade2 = 17

if idade >= 65:
    #print(idade >= 18)
    print(f'{nome} é idoso')
elif idade >= 18:
    print(f'{nome} é adulto')
else:
    print(f'{nome} é menor de idade')

if idade2 >= 18:
    print(f'{nome2} é maior de idade')
else:
    print(idade2 >= 18)
    print(f'{nome2} é menor de idade')

Loops
    - Loops são funções do sistema que fazem repetição de um bloco do código
    Temos 2 tipos de Loops:
        -FOR: (para) ele é utilizado para uma repetição com um número DEFINIDO de vezes, ou seja, quando
        o programador quer estipular um número X de repetições.

        Exemplo:
# Loop com for
total = 0
# range(4) = [0, 1, 2, 3]
for n in range(4):
    nota = float(input(f"Digite a sua nota do {n + 1} bimestre"))
    total += nota  # total = total + nota
print(f'A sua média é {total/4}')


        -WHILE: (enquanto) é utilizado para repetir um bloco de comando um número INDEFINIDO de vezes, ou seja
        só irá parar de repetir quando uma condição for satisfeita.

# Loops com while
# Forma 1
total = 0
nota = 0
cont = 0
while nota >= 0:  # Repete enquanto a expressão for VERDADEIRA
    cont += 1
    nota = float(input(f"Digite a sua {cont} nota: "))
    total += nota  # total = total + nota

print(f'A sua média é {total/cont}')

# Forma 2 - While
cont = 0
total = 0
while True:
    nota = float(input(f"Digite a {cont + 1} nota: "))
    if nota < 0:
        break  # Esse comando força a parada do loop
    total += nota
    cont += 1

print(f'A sua média é {total/cont}')


Coleções (listas)

# Coleções (listas)
# Utilizamos [] para representar listas, com listas é possível:
# armazenar novas informações
# excluir elementos da lista
# organizar a lista
# acessar um item da lista por meio de indexação
# pesquisar um item na lista

lista = []
lista2 = list(range(10))
lista3 = ['F', 'e', 'l', 'i', 'p', 'e']
lista4 = ['BATIMA', True, [1, 2, 3], 10, 8.5]
lista5 = [10, 8, 15, 2, 3, 6, 1, 10, 11]

print(lista)
print(lista2)
print(lista3)
print(lista4)
# Adicionar elemtnos no meio da lista
# utilizamos o comando insert()
lista4.insert(1, 'Robin')
print(lista4)
# Adicionar elementos no fim da lista
# Utilizamos o comando append()
lista.append('Novo dado')
print(lista)
lista.append(100)
print(lista)

# Excluir elementos da lista
# Utilizamos o comando pop()
removido = lista2.pop()
print(lista2)
lista2.pop()
print(lista2)
print(removido)

# Organizar a lista
# Utilizamos o comando sort()
print(lista5)
lista5.sort()
print(lista5)

# Acessar um item na lista por indexação
print(lista3[2])  # basta inserir o número entre colchetes
print(lista3[-1])  # Imprime de forma inversa

print('e' in lista3)
print('P' in lista3)

if 'e' in lista3:
    print("Encontrei o 'e' na lista")

pow(10, 0.5) # = 10**0.5


# PRÁTICA
# Construa um algoritmo que através da fórmula de bhaskara calcule o delta, x' e x''

#  ax² + bx + c  = 0
# Delta >= 0
while True:
    a = int(input("Digite o valor de 'a': "))
    b = int(input("Digite o valor de 'b': "))
    c = int(input("Digite o valor de 'c': "))

    delta = (b**2) - (4 * a * c)
    print(delta)

    if delta > 0:
        print("Delta maior que zero, então teremos x' e x'', sendo:")
        x1 = (-b + (delta**0.5))/(2 * a)
        x2 = (-b - (delta**0.5))/(2 * a)
        print(f"x': {x1}")
        print(f"x'': {x2}")

    elif delta == 0:
        print("Delta igual a zero, então teremos apenas x, sendo:")
        x = (-b + (delta ** 0.5)) / (2 * a)
        print(f"x = {x}")

    else:
        print("Delta é negativo, portanto não há como descobrir x' e x''! ")

    sair = input('Deseja sair?(s/n)')
    if sair.lower() == 's':
        break

"""
