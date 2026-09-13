#b)	distância de um raio distância = tempo x 340 ( 340 = velocidade do som no ar em metros por segundo)
import time

validation = True
valueDistance = 0
timeValue = 0

while(validation):
    try:
        value = float(input("\nDigite o valor tempo em segundos: ").replace(",", "."))
        timeValue = value
        validation = False
    except:
        print("\nValor digitado é invalido, digite novamente")
        time.sleep(2)

valueDistance = 340 * timeValue
print(f"\n\nEm {timeValue:.2f}seguntos, um riao percorre uma distância de {valueDistance:.2f}metros")


