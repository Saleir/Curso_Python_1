from os import system
system('cls')

import requests
# Trazer informações via API da loja FakeStoe
produtos = requests.get('https://fakestoreapi.com/products')
# Converter informções para Json
produtos = produtos.json()

print(f'{'ID':<3} | {'PRODUTO':<97} | {'PREÇO R$':<6}')
print('+' * 112)

for produto in produtos:
    # Recuperar informações do produto
    id = produto['id']
    title = produto['title']
    price = produto['price']
    #  Exibir informações da lista
    print(f'{id:<3} | {title:<97} | {price:<6}' )
    print('-' * 112)

