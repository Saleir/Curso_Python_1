from os import system
system('cls')
#from os import system
#system('cls') = limpa a tela com os dados no terminal

# Funções para trabalhar coom textos
nomecompleto = input('Digite seu nome completo: ')
# len = length - contta o número de caracteres
print('- Função para contar caracteres: ', len(nomecompleto))
print('- Função para texto maiúsculo: ', nomecompleto.upper())
print('- Função para texto minusculo: ', nomecompleto.lower())
print('- Função para primeiro maiúsculo: ', nomecompleto.capitalize())
print('- Função para primeira letra de cada palavra maiusculo: ', nomecompleto.title())
print('- Função para remover espaços em branco antes e depois do texto: ', nomecompleto.strip())
print('- Quebrar o texto a cada espaço em branco:', nomecompleto.split()) 
espaco = nomecompleto.find(' ')
print('- Primeira letra:  ', nomecompleto[0:espaco] )
print('- Remover espaços vazios: ' , nomecompleto.replace(' ',''))
print('- Contar letras sem espaços: ' , len(nomecompleto.replace(' ','')))
#novonome = nomecompleto.replace('Saleir','Mateus')
#print(novonome)

# find = procura um caractere no texto
# strip = remover espaços em branco antes e depois do texto
# title = primeira letra de cada palavra maiusculo
# upper = texto com letras maiusculas
# lower = texto com letras minisculas
# capitalize = texto com a primeira letra maiusscula