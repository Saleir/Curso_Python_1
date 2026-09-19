# CALCULAR ÁREA DE UM RETÂNGULO
base = input('Informe o valor da base em metros: ')
alt = input('Informe o valor da altura em metros: ')

print('Base é numérico?' , base.isnumeric()) 
print('Altura é numérico?' , alt.isdecimal())

area = float(base) * float(alt)
# float =  ponto flutuante , ou seja , aceita casas dcimais.
print('Base: {} , Altura: {}, Área: {}' . format(base, alt, area))
print( 'A área do retângulo é de {}' . format(area) ,'m²')