"""
V 0.1 do algoritmo para resoluções de fórmulas de física

Para organização do código, vamos separar em funções
# Funções são pequenos trechos de código que resolvem UM problema
Para iniciar uma função em Python digitamos:

def nome_da_funcao(parâmetros):  #Parâmetros são opcionais

    Código da função
    Código da função
    Código da função
    Código da função
    Código da função
    return None

Fora da função

# Para chamar uma função, basta digitar o seu nome e colocar os parâmetros entre parênteses
print("asdasdsa")
calculo_de_densidade(massa,volume)  # Função com parâmetros
calculo_de_densidade()  # Função sem parâmetros
"""


def calculo_de_densidade():  # Criando uma função sem entrada que retorna a densidade

    """
    Função para cálculo de densidade
    :return: FLOAT valor da densidade
    """
    massa = float(input("Digite o valor da massa: "))
    volume = float(input("Digite o valor do volume: "))
    d = massa/volume
    return d


def velocidade_media():
    """
    Calcula a velocidade média (ainda sem unidades de medida) todo unidades de medida
    :return: float velocidade média
    """
    print("Fórmula para cálculo da velocidade média.")
    espaco = float(input("Digite o valor para espaço: "))
    tempo = float(input("Digite o valor para o tempo: "))

    vm = espaco / tempo
    return vm
