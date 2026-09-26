from os import system
system('cls')

def Somar(x,y):
    try:
        print(f'A soma entre os números é de: {x} + {y}={x+y}')
    except:
            print('ERRO desconhecido!')
def Subtrair(x,y):
    try:    
        print(f'A subtração entre os números é de: {x} - {y}={x-y}')
    except:
            print('ERRO desconhecido!')
def Multiplicar(x,y):
    try:
         print(f'A multiplicação entre os números é de: {x} * {y}={x*y}')
    except:
            print('ERRO desconhecido!')
def Dividir(x,y):
    # try tem a função de tentar e except é a excessão do erro
    try:
        print(f'A divisão entre os números é de: {x} / {y}={x/y} ')
    except ZeroDivisionError as erro:
        print('Impossível divisão por ZERO')
    



opcao = ' '

while opcao != 'X':
    system('cls')
    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Informe o segundo número: '))
    opcao = int(input ('''
    Opções:
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicar
    [4] - Dividir
    Escolha uma opção acima: '''))
    if opcao == 1:
        Somar(num1, num2)
    elif opcao == 2:
        Subtrair(num1, num2)
    elif opcao == 3:
        Multiplicar(num1, num2)
    elif opcao == 4:
        Dividir(num1, num2)
    else:
        print("Número inválido")

    opcao = input('Aperte X para finalizar ou qualquer outra tecla para continuar: ').upper()





