from os import system
system('cls')

inss = 0
irpf = 0
salario = float(input('Digite o salário em Reais (R$): ').replace(',','.'))

print('1 - empregado')
print('2 - contribuinte')
tipo = int(input('Digite se é empregado ou contribuinte: '))

if salario > 8475.55: 
 if tipo == 1:
  inss = 988.07
 else:
  inss = 932.31

elif salario > 4354.27: 
 aliquota_inss = 0.14 
 parcela_inss = 198.49
 #inss = salario * aliquota_inss - parcela_inss
# inss = 0.14 * salario - 198.49
elif salario > 2902.84: 
 aliquota_inss = 0.12 
 parcela_inss = 111.40
 #inss = salario * aliquota_inss - parcela_inss
# inss = 0.12 * salario - 111.40
elif salario > 1621.00: 
 aliquota_inss = 0.09 
 parcela_inss = 24.32
 #inss = salario * aliquota_inss - parcela_inss 
# inss = 0.09 * salario - 24.32
else: 
 aliquota_inss = 0.075 
 parcela_inss = 0
 # inss = 0.075 * salario
inss = salario * aliquota_inss - parcela_inss  
salario_inss = salario - inss

if salario_inss > 4664.68:
 aliquota_irpf = 0.275
 parcela_inss = 908.73
 #irpf = 0.275 * salario_inss - 908.73
elif salario_inss> 3751.05:
 aliquota_irpf = 0.225
 parcela_irpf = 675.49
 #irpf = 0.225 * salario_inss - 675.49
elif salario_inss > 2826.65:
 aliquota_irpf = 0.15
 parcela_irpf = 394.16 
 #irpf = 0.15 * salario_inss - 394.16
elif salario_inss > 2428.80:
 aliquota_irpf = 0.075
 parcela_irpf = 182.16 
 #irpf = 0.075 * salario_inss - 182.16
else:
 aliquota_irpf = 0
 parcela_irpf = 0 
 #irpf = 0 * salario_inss

irpf = salario_inss * aliquota_irpf- parcela_irpf  
total = salario_inss - irpf



print(f'Salário base para desconto INSS: R$ {salario_inss:.2f}')
print(f'Aliquota INSS: {aliquota_inss*100:.1f} %')
print(f'Aliquota IRPF: {aliquota_irpf*100:.1f} %')
print(f'Parcela dedução:R$ {parcela_inss:.2f}')
print(f'Salário com desconto IRPF: R$ {total:.2f}')

print('Seu desconto do INSS é de R$ {:.2f} do salário bruto R$ {:.2f} com desconto de INSS fica R$ {:.2f} de salário líquido você receberá R$ {:.2f}'
      .format(inss, salario, salario_inss,total).replace('.', ','))
# print('Seu desconto do INSS é de R$ {:.2f} do salário bruto R$ {:.2f} e você vai receber R$ {:.2f} de salário líquido' . format(inss,salario,liquido))

#Até R$ 1.621,00 7, 5% R$ 0,00
# De R$ 1.621,01 até R$ 2.902,84 9% R$ 24,32
# De R$ 2.902,85 até R$ 4.354,27 12% R$ 111,40
# De R$ 4.354,28 até R$ 8.475,55 14% R$ 198,49