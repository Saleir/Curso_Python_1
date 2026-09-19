from os import system
import time
system('cls')
# Inicia a contagem do multiplicando
for i in range(1,11): 
    #Limpa a variável linha a cada iteração do laço externo   
    linha =''
    for u in range(1,11):
       #vai armazenando o resultado da multiplicação do multiplicando (i) com o multiplicador (u) na variável linha
       linha += f'{i*u: >4}'
# : >4 é uma formatação de string que alinha o resultado da multiplicação à direita, ocupando 4 espaços, para que os resultados fiquem alinhados na tela
# : <4 é uma formatação de string que alinha o resultado da multiplicação à esquerda, ocupando 4 espaços, para que os resultados fiquem alinhados na tela    

    # Mostra os resulatdos da tabuada do multiplicando   
    print(linha)
    time.sleep(1)

# += é um operador de atribuição que adiciona o valor da direita ao valor da esquerda e atribui o resultado à variável da esquerda


    