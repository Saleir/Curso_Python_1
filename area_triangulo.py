# CALCULAR ÁREA DE UM TRIÂNGULO
base = input('Informe o valor da base em metros: ')
alt = input('Informe o valor da altura em metros: ')
div = 2

# print('Base é numérico?' , base.isnumeric()) 
# print('Altura é numérico?' , alt.isdecimal())

if base.isnumeric: 
    print('Base é númerico') 
else: 
    print('Base não é númerico')
if alt.isnumeric: 
    print('sim') 
else: 
    print('não')

area = float(base) * float(alt) / div
# float =  ponto flutuante , ou seja , aceita casas dcimais.
print('Base: {} , Altura: {}, Área: {}' . format(base, alt, area))
print( 'A área do Triângulo é de {}' . format(area) ,'m²')