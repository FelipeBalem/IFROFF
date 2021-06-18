"""
Revisão if else

# Faça um algoritmo que receba um nome de uma cor e informe se ela é uma cor primária
# ou não primária.
# Cores primárias: Vermelho amarelo e azul

# Forma 1
# Entrada de dados
cor = input("Digite uma cor: ")  # Usuário digita o nome da cor

if cor == "vermelho":
    print(f"{cor} é uma cor primária.")
elif cor == "azul":
    print(f"{cor} é uma cor primária.")
elif cor == "amarelo":
    print(f"{cor} é uma cor primária.")
else:
    print(f"{cor} NÃO é uma cor primária. ")


# Forma 2
cor = input("Digite uma cor: ")
print(cor)
cor = cor.lower()
print(cor)

if cor == "vermelho" or cor == "azul" or cor == "amarelo":
    print(f'{cor} é uma cor primária. ')
else:
    print(f'{cor} NÃO é uma cor primária. ')

# utilizando o OR e AND
# Algoritmo para mistura de cores
print("Digite apenas cores primárias")
cor1 = input("Digite a primeira cor da mistura: ")
cor2 = input("Digite a segunda cor da mistura: ")

if cor1 == "vermelho" and cor2 == "amarelo" or cor1 == "amarelo" and cor2 == "vermelho":
    print(f'{cor1} com {cor2} resulta em laranja.')

elif cor1 == "vermelho" and cor2 == "azul" or cor1 == "azul" and cor2 == "vermelho":
    print(f'{cor1} com {cor2} resulta em roxo.')

elif cor1 == "azul" and cor2 == "amarelo" or cor1 == "amarelo" and cor2 == "azul":
    print(f'{cor1} com {cor2} resulta em verde.')

else:
    print(f'{cor1} ou {cor2} são cores inválidas.')

"""
