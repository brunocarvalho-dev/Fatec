#// b)    Ler  uma  temperatura  em  graus  Fahrenheit  e  apresentá-la  convertida  em  graus  Celsius.
#//      A  fórmula  de conversão é C ← (F - 32) * (5/9) , sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
import time
celcius = 0
validador = True
def verificacao_valor(valor):
    if (valor < (-469.57)):
        valor = True
    else:
        valor = False
    return valor

while validador:
    try:
        fahrenheit = float(input('\ndigite o valor do fahrenheit: ').replace(',','.'))
        if (validador and (fahrenheit < -469.57)):
                    print("\nvalor inválido\n")
                    time.sleep(2)
    except:
        print("valor invalido, digite novamente")
        time.sleep(2)
    

celcius = ((fahrenheit - 32) * (5/9))
resposta = ("O valor "+str(celcius)+"ºC é "+str(fahrenheit)+" em Fahrenheit")

print(resposta)