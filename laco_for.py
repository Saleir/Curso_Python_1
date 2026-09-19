from os import system
import time
system('cls')

numero = int(input('Informe um número maior que 0 : '))
# Verifica se o número é positivo ( se digitar número negativo ele trava por não encontrar)
if numero <= 0:
    print('Número inválido!')
else:
    # Iniciando Laço For
    for i in range(numero):
        print(f'Valor da variável i: {i}')
        time.sleep(2) # dorme por 2 segundos