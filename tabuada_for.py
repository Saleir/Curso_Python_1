from os import system
import time
system('cls')

numero = int(input('Informe um número: '))
for i in range(1,21):
    print(f'{numero} * {i} = {numero*i}')
    time.sleep(2)
