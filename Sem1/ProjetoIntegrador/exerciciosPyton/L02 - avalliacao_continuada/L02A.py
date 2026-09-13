#a)	área do triângulo: área = base x altura/2 
import time

validation = True
valueAltura = 0
valueBase = 0

while(validation):
    try:
        value = float(input("\nDigite o valor da altura em metros ").replace(",", "."))
        valueAltura = value
        while(validation):
            try:
                value = float(input("\nDigite o valor da base em metros: ").replace(",", "."))
                valueBase = value
                validation = False
            except:
                print("\nValor digitado da base é invalido, digite novamente")
                time.sleep(2)

    except:
        print("\nValor digitado da altura é invalido, digite novamente")

valueArea = (valueBase*valueAltura)/2

print(f"\n\nO valor total da área do triângulo é: {valueArea:.2f} m²")