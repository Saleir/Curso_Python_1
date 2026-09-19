# Converter moedas  REAL / DÓLAR / EURO
from os import system
system('cls')

real = float(input('Digite o valor em Reais (R$): '))

print('Escolha a moeda pra coversão: ')
print('1 - Dólar (US$)')
print('2 - EURO (€)')
print('3 - Kwanza (Kz)')
print('4 - Won (₩)')
print('5 - Peso Colombiano (COP)')
print('6 - Iene (¥)')
opcao = int(input('Opção:'))

if opcao == 1:
    dolar = real /5.13
    print('R$ {:.2f} equivale a US$ {:.2f}'. format(real,dolar))
elif opcao == 2:
    euro = real /5.93
    print('R$ {:.2f} equivale a € {:.2f}' . format(real,euro))
elif opcao == 3:
    kwanza = real /0.0056
    print('R$ {:.2f} equivale a kZ {:.2f}' . format(real,kwanza))
elif opcao == 4:
    won = real /0.0038
    print('R$ {:.2f} equivale a ₩ {:.2f}' . format(real,won))
elif opcao == 5:
    peso = real /0.0016
    print('R$ {:.2f} equivale a COP {:.2f}' . format(real,peso))
elif opcao == 6:
    iene = real /0.033
    print('R$ {:.2f} equivale a ¥ {:.2f}' . format(real,iene))
else:
    print('Opção inválida!')
    # :.2f = Formatação para 2 casas decimais