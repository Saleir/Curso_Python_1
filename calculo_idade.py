from os import system
from datetime import datetime

system('cls')

# Pedir data de nascimento do usuário
data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaa): ")
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

# Dta atual
data_atual = datetime.today()

# Calcular idade
idade = data_atual.year - data_nascimento.year
print(f'Sua idade é: {idade} anos.')