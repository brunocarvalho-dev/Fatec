
#a)    Ler  uma  temperatura  em  graus  Celsius  e  apresentá-la  convertida  em  graus  Fahrenheit.
#   A  fórmula  de conversão é F ← (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
import time
validador = True
celcius
def verificacao_valor(valor):
    if (valor > (-273.15)):
        valor = False
    else:
        valor = True
    return valor

while(validador):
    try:
        celcius = float(input("\ndigite o valor ºC (graus Celcius): ").replace(",","."))
        validador = verificacao_valor(celcius)
        if (validador and (celcius < -273,15)):
            print("\nvalor inválido\n")
            time.sleep(2)
        else:
            time.sleep(2)

    except:
        print("\nvalor inválido")

fahrenheit = str((9*celcius+160)/5)
print("\no valor "+celcius+"ºC é "+ fahrenheit+" fahrenheit")