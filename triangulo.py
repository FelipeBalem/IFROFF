"""
Algoritmo para descobrir se 3 valores de arestas formam um triângulo
e qual o tipo (equilátero, isósceles e escaleno). O algoritmo deve repetir até
o usuário digitar 'sair'.

sair = False
while sair == False:
    a = float(input("Digite o tamanho do primeiro lado: "))
    b = float(input("Digite o tamanho do segundo lado: "))
    c = float(input("Digite o tamanho do terceiro lado: "))

    if a + b < c or a + c < b or b + c < a:
        print(f"Os valores {a}, {b} e {c} NÃO formam um triângulo!")

    elif (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
        print(f"Os valores {a}, {b} e {c} formam um triângulo isósceles!")

    elif a == b and b == c:
        print(f"Os valores {a}, {b} e {c} formam um triângulo equilátero!")

    elif a != b and a != c and b != c:
        print(f"Os valores {a}, {b} e {c} formam um triângulo escaleno!")

    sair = input("Digite 'sair' para sair ou qualquer tecla para continuar. ")
    if sair == 'sair':
        sair = True
    else:
        sair = False

"""
sair = 0

while not sair:  # while sair == False:
    a = float(input("Digite o tamanho do primeiro lado: "))
    b = float(input("Digite o tamanho do segundo lado: "))
    c = float(input("Digite o tamanho do terceiro lado: "))

    if a + b < c or a + c < b or b + c < a or a <= 0 or b <= 0 or c <= 0:  # Se não for um triângulo
        print(f"Os valores {a}, {b} e {c} NÃO formam um triângulo!")

    else:
        # if (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
        if a == b != c or b == c != a or a == c != b:
            print(f"Os valores {a}, {b} e {c} formam um triângulo isósceles!")

        elif a == b == c:
            print(f"Os valores {a}, {b} e {c} formam um triângulo equilátero!")

        else:  # if a != b != c and a != c:
            print(f"Os valores {a}, {b} e {c} formam um triângulo escaleno!")

    sair = input("Digite 1 para sair: ")
    if sair == 1:
        break
    else:
        sair = 0
