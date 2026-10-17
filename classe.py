from os import system
from datetime import datetime
#Iniciando a classe Servico

class Servico:
    # Construtor/Inicialize da classe
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco
        self.data = datetime.today().strftime("%d/%m/%Y")
        self.horario = datetime.now().strftime("%H:%M:%S")
    # Metodo para exibir os dados do serviço
    def exibir_dados(self): 
        print(f'Data : {self.data}')
        print(f'Hora: {self.horario}')
        print(f'Descrição: {self.descricao}')
        print(f'Preço: R${self.preco:.2f}')
        
    # Método para salvar os dados em txt
    def salvar_historico(self):
        # Abre o arquivo em modo de escrita (append) para adicionar novos registros
        # utf-8 é usado para suportar caracteres especiais
        # with - enquanto utilizar o comando para abrir o arquivo
        with open('historico_servicos.txt','a', encoding= 'utf-8') as f:            
            f.write(f'Data {self.data}\n')
            f.write(f'Horário {self.horario}\n')
            f.write(f'Descrição: {self.descricao}\n')
            f.write(f'Preço: {self.preco:.2f}\n')
            f.write('_' * 40 + '\n')
        

# Iniciando o codigo principal
print(' == CADASTRO DE SEWRVIÇOS == ')

continuar =  'S'

while continuar.upper() != 'X':
    descricao = input("Informe a descrição do serviço: ")
    preco = input("Informe o preço do serviço:R$ ")

    try:
        preco =float(preco)
    except ValueError:
        print('Preço inválido. Por favor, insira um número válido.')
        continue

    system ('cls')
    # Criando uma instância da classe Servico
    servico = Servico(descricao, preco)
    #Exibindo os dados do servico
    servico.exibir_dados()
    # salvar dados em arquivo txt
    servico.salvar_historico()
    print('_' * 40)


    continuar = input('Tecle "ENTER" para continuar ou "X" para sair: ')
    system('cls')