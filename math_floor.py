from os import system
import math
system('cls')

# Uma caminhão trasnporta ?? toneladas de carga
# Quantas viagens ele precisa fazer somente com a capacidade máxima?


capacidade_total = int(input('Carga Total do caminhão (em toneladas): '))
carga_viagem = float(input('Carga para viagem (em toneladas): '))

qtde_viagens =math.floor(carga_viagem/capacidade_total)
carga_restante = carga_viagem - (capacidade_total * qtde_viagens)

print(f'Qtde de viagens carga Máxima: {qtde_viagens}')
print(f'Carga restante: {carga_restante:.2f}')

 