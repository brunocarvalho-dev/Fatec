#c)    Calcular e apresentar o valor do volume de uma lata de óleo, 
#utilizando a fórmula:AlturaRaioVolume**2π←
import math
validador=True
def verificacao_valor(valor):
    if (valor > 0):
        valor = False
    else:
        valor = True
    return valor

while validador:
    try:
        raio = (input('\ndigite o valor do raio em metros: ').replace(',','.'))
        validador = verificacao_valor(float(raio))
        raio = float(raio)
    except:
        print("valor invalido, digite novamente: ")
    

validador=True
while validador:
    try:
        altura = (input('\ndigite o valor da alturaem metros: ').replace(',','.'))
        validador = verificacao_valor(float(altura))
        altura= float(altura)
    except:
        print("valor invalido, digite novamente: ")

volume = pow(raio, 2)*math.pi*altura
print('o volume do cilindro é : %.2f m³' % volume)