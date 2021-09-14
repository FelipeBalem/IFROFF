"""
Tela principal do física fácil

"""
from fisica_v02 import calculo_densidade

while True:
    print('Escolha uma das opções abaixo:')
    escolha = input("1) Cálculo de densidade:\n"
                    "2) Velocidade média\n"
                    "3) Calor sensível\n"
                    "s) sair\n")

    if escolha == '1':
        calculo_densidade()
    elif escolha == '2':
        print('Função ainda não implementada')
    elif escolha == '3':
        print('Função ainda não implementada')
    elif escolha.lower() == 's':
        break
    else:
        print('Comando inválido.')

print('Finalizando programa')
