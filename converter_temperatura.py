from os import system
system('cls')

celsius = float(input('Digite o valor da temperatura em Celsius (°C): '))

print('Escolha a tempetatura pra coversão: ')
print('1 - Kelvin (K)')
print('2 - Fahrenheit (°F)')

opcao = int(input('Opção:'))

if opcao == 1:

    kelvin = celsius + 273.15
# fórmula conversão celsius em kelvin 0 °C + 273,15 = 273,15 K
  
    print('°C {:.2f} equivale a K {:.2f}'.format(celsius, kelvin))

elif opcao == 2:
# fórmula conversão celsius em fahrenheit (0 °C × 9/5 ou 1.8) + 32 = 32 °F
    fahrenheit = celsius * 9/5 + 32

    print('°C {:.2f} equivale a °F {:.2f}'.format(celsius, fahrenheit))
else:

    print('Opção inválida!')
