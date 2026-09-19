from os import system
system('cls')

numero = int(input('Digite um número: '))
# procentagem em cálculo ele faz a divisão e retorna o resto do cálculo
resto = numero % 2
# um = atribui um valor a variavel
# 2 == para comparar valores ioguais
# ! para comparar valores DIFERENTES
# < para comparar valores MENORES
# > para comparar valores MAIORES
# >= para comparar valores MAIORES OU IGUAIS

if resto == 0:
    print('O número {} é PAR!' . format(numero))
else:
    print('O número {} é ÌMPAR' . format(numero))


