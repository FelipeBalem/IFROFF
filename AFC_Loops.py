"""soma = 0
for i in range(50):
    numero = int(input(f"Digite o número {i+1}/50: "))
    soma = soma + numero

media = soma/50
print(f"A média é {media}")
"""

numero = None
soma = 0
contador = 0
while numero != 0:
    numero = int(input(f"Digite o {contador + 1}º número: "))
    if numero != 0:
        soma = soma + numero
        contador = contador + 1

media = soma/contador
print(f"A média é {media}")