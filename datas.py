from datetime import datetime
from os import system
system('cls')

print(datetime.now())

# Pegar data atual do sistema
data_atual = datetime.now()
print(f'Data atual {data_atual}')
print(type(data_atual))

#Criar data (Ano,Mês,Dia)
data_criada = datetime(1982,5, 12, 10, 28, 11, 123456)
print(f'Data criada: {data_criada.date()}')
print(type(data_criada))

# Pedir data ao usúario
data_usuario = input("Digite uma data no formato dd/mm/aaaa: ")
print(f'Data usuário: {data_usuario}')
print(type(data_usuario))

#Converter string em data
data_convertida = datetime.strptime(data_usuario, '%d/%m/%Y')
