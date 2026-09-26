from os import system
import random
# random = utilizar escolha aleatória
system('cls')

continua = 'S'

while continua == 'S':

    computador = random.randint(0, 2)
    jogador = int(input('''Opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura
Escolha uma opção: '''))
    system('cls')

    if jogador >=0 and jogador <=2:
        pecas = ('Pedra','Papel','Tesoura')
        print(f'Computador escolheu {pecas[computador]}')
        print(f'Você escolheu {pecas[jogador]}')

        tabela = ((0, 1, -1),(-1, 0, 1),(1, -1, 0)) 
        jogada = tabela[computador][jogador]

        if jogada ==0:
            resultado = "Deu empate entre vocês"
        elif jogada ==1:
            resultado = "Você ganhou!"
        elif jogada ==-1:
            resultado = "Você perdeu!"
        print(resultado)

    else:
        print("Jogador escolheu uma opção INVÁLIDA!")
    continua = input("Digite [S] para jogar novamente : ").upper()
