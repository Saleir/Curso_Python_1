from os import system
system('cls')

# calculo de IMC
# Pede para o usuario digitar a altura
altura = input('Digite a sua altura em metros: ')
# Subtitui virgula por ponto e converte em decimal
altura = float(altura.replace(',','.'))
# Pede para o usuario digitar o peso
# Substitui virgula por ponto e converte em decimal
peso = float(input('Diigite a seu peso em Kg: ').replace(',','.'))
# ** expoente
imc = peso / (altura ** 2)
# print('IMC igual a :', imc)
# print('Seu IMC: {} {} {}' . format(imc))
print(f'Seu IMC: {imc:.2f}')
# {imc:.2f} = faz aparecer apenas 2 casas decimais no resultado

if imc < 18.5:
    print('Peso abaixo do normal ')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 34.9:
    print('Obesidade grau I')
elif imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade Mórbida')