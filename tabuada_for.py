from os import system
import time
system('cls')
# for i in range cria laço de repetição, range(1,21) significa que vai de 1 até 20
numero = int(input('Informe um número: '))
for i in range(1,21):
    print(f'{numero} * {i} = {numero*i}')
    time.sleep(2)
# time.sleep(2) faz o programa esperar 2 segundos antes de continuar a execução do código
# print(f'{numero} * {i} = {numero*i}') imprime o resultado da multiplicação do número informado pelo usuário com o valor de i
# fim e inicio do laço é indicado por () e os dois pontos (:) no final da linha
# identação é importante para indicar o que está dentro do laço de repetição
