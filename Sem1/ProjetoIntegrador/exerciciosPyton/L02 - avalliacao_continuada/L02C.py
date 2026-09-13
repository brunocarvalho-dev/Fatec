import time
import math

validation = True
G = 9.8
valueAltura = 0
valueDrop = 0

while(validation):
    try:
        value = float(input("\nDigite o valor da altura em metros ").replace(",", "."))
        valueAltura = value
        validation = False
    except:
        print("\nValor digitado da altura é invalido, digite novamente")
        time.sleep(2)
valueDrop = (math.sqrt(2*valueAltura))/G

print(f"\n\nUm objeto caindo a {valueAltura:.1f}metros leva {valueDrop:.2f}segundos para chear ao chão")