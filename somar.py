# Receber 2 números do usúario , realizar a soma entre eles e exibir
# int = transforma texto em número inteiro
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
num3 = input('Informe o terceiro número: ')
soma = int(num1) + int(num2) +int(num3)
# print('A soma entre' , num1 , 'e' , num2 , 'é de' , soma ) - exemplo 1 para exibir o resulatdo.
print('A soma de entre {} , {} e {} é de {}' . format(num1, num2, num3, soma))
