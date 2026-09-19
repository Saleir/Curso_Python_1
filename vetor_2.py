from os import system
system('cls')

nomes= []
total= int(input("Quantos nomes deseja cadastrar? "))

for i in range(0,total):
    system('cls')
    nomes.append(input('Digite um nome: '))
    system('cls')

for i in range(0,total):
    print(f'{i} - {nomes[i]}')


#for i in range(0,5):
 #   nomes[i]=input('Digite um nome: ')
