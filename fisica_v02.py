"""
Funções de física versão 2
"""


def calculo_densidade():
    def valor_massa():
        print('Então vamos descobrir o valor da massa, para isso preciso que você: ')
        v = float(input("Digite o valor do volume"))
        d = float(input('Digite o valor da densidade'))
        return v * d

    def valor_volume():
        print('Então vamos descobrir o valor do volume, para isso preciso que você: ')
        m = float(input("Digite o valor da massa"))
        d = float(input('Digite o valor da densidade'))
        return m/d

    def valor_densidade():
        print('Então vamos descobrir o valor da densidade, para isso preciso que você: ')
        m = float(input("Digite o valor da massa"))
        v = float(input('Digite o valor do volume'))
        return m/v

    def help_densidade():
        print('Densidade é blablabla')

    while True:
        opcao = input("Você quer descorbrir \n(m)massa,\n(v)volume,\n(d)densidade?\nDigite (h) para ajuda)\n")
        if opcao.lower() == 'm':
            print(f' Valor da massa = {valor_massa()}')
        elif opcao.lower() == 'v':
            print(f' Valor do volume = {valor_volume()}')
        elif opcao.lower() == 'd':
            print(f'Valor da densidade: {valor_densidade()}')
        elif opcao.lower() == 'h':
            help_densidade()
        else:
            print('Comando inválido')

        sair = input("Deseja sair? s/n")
        if sair.lower() == 's':
            break

