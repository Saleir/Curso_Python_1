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

    dolar = real / 5.13

    print('R$ {:.2f} equivale a US$ {:.2f}'.format(real, dolar))

elif opcao == 2:

    euro = real / 5.93

    print('R$ {:.2f} equivale a € {:.2f}'.format(real, euro))

elif opcao == 3:

    kwanza = real / 0.0056

    print('R$ {:.2f} equivale a Kz {:.2f}'.format(real, kwanza))

elif opcao == 4:

    won = real / 0.0038

    print('R$ {:.2f} equivale a ₩ {:.2f}'.format(real, won))

elif opcao == 5:

    peso_colombiano = real / 0.0016

    print('R$ {:.2f} equivale a COP {:.2f}'.format(real, peso_colombiano))

elif opcao == 6:

    iene = real / 0.033

    print('R$ {:.2f} equivale a ¥ {:.2f}'.format(real, iene))

elif opcao == 7:

    libra = real / 6.90

    print('R$ {:.2f} equivale a £ {:.2f}'.format(real, libra))

elif opcao == 8:

    peso_argentino = real / 0.0045

    print('R$ {:.2f} equivale a ARS {:.2f}'.format(real, peso_argentino))

elif opcao == 9:

    peso_chileno = real / 0.0055

    print('R$ {:.2f} equivale a CLP {:.2f}'.format(real, peso_chileno))

elif opcao == 10:

    peso_mexicano = real / 0.29

    print('R$ {:.2f} equivale a MXN {:.2f}'.format(real, peso_mexicano))

elif opcao == 11:

    sol = real / 1.45

    print('R$ {:.2f} equivale a PEN {:.2f}'.format(real, sol))

elif opcao == 12:

    boliviano = real / 0.74

    print('R$ {:.2f} equivale a BOB {:.2f}'.format(real, boliviano))

elif opcao == 13:

    guarani = real / 0.00075

    print('R$ {:.2f} equivale a PYG {:.2f}'.format(real, guarani))

elif opcao == 14:

    peso_uruguaio = real / 0.13

    print('R$ {:.2f} equivale a UYU {:.2f}'.format(real, peso_uruguaio))

elif opcao == 15:

    dolar_canadense = real / 3.75

    print('R$ {:.2f} equivale a CAD {:.2f}'.format(real, dolar_canadense))

elif opcao == 16:

    dolar_australiano = real / 3.40

    print('R$ {:.2f} equivale a AUD {:.2f}'.format(real, dolar_australiano))

elif opcao == 17:

    franco_suico = real / 6.30

    print('R$ {:.2f} equivale a CHF {:.2f}'.format(real, franco_suico))

elif opcao == 18:

    coroa_dinamarquesa = real / 0.80

    print('R$ {:.2f} equivale a DKK {:.2f}'.format(real, coroa_dinamarquesa))

elif opcao == 19:

    coroa_sueca = real / 0.55

    print('R$ {:.2f} equivale a SEK {:.2f}'.format(real, coroa_sueca))

elif opcao == 20:

    coroa_norueguesa = real / 0.52

    print('R$ {:.2f} equivale a NOK {:.2f}'.format(real, coroa_norueguesa))

elif opcao == 21:

    rublo = real / 0.063

    print('R$ {:.2f} equivale a RUB {:.2f}'.format(real, rublo))

elif opcao == 22:

    rupia_indiana = real / 0.061

    print('R$ {:.2f} equivale a INR {:.2f}'.format(real, rupia_indiana))

elif opcao == 23:

    yuan = real / 0.72

    print('R$ {:.2f} equivale a CNY {:.2f}'.format(real, yuan))

elif opcao == 24:

    dolar_hong_kong = real / 0.65

    print('R$ {:.2f} equivale a HKD {:.2f}'.format(real, dolar_hong_kong))

elif opcao == 25:

    baht = real / 0.15

    print('R$ {:.2f} equivale a THB {:.2f}'.format(real, baht))

elif opcao == 26:

    ringgit = real / 1.20

    print('R$ {:.2f} equivale a MYR {:.2f}'.format(real, ringgit))

elif opcao == 27:

    rupia_indonesia = real / 0.00030

    print('R$ {:.2f} equivale a IDR {:.2f}'.format(real, rupia_indonesia))

elif opcao == 28:

    rand = real / 0.30

    print('R$ {:.2f} equivale a ZAR {:.2f}'.format(real, rand))

elif opcao == 29:

    lira_turca = real / 0.14

    print('R$ {:.2f} equivale a TRY {:.2f}'.format(real, lira_turca))

elif opcao == 30:

    shekel = real / 1.50

    print('R$ {:.2f} equivale a ILS {:.2f}'.format(real, shekel))

else:

    print('Opção inválida!')
