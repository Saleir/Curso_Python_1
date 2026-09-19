from os import system
system('cls')

numeros = ('zero','um','dois','très','quatro','cinco','seis','sete','oito','nove')
dez = ('dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove')
dezenas = ('vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa')

numero =int(input("Informe um número de 0 a 99: "))

if numero >= 0 and numero <= 99:

    if numero <10:
        print(numeros[numero])
    elif numero <20:
        print(dez[numero-10])
    



else:
    print("Número inválido!")


