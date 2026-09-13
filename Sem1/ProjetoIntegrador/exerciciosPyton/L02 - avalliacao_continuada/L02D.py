#list = [10,20,30,'hi', 44]
#print(*list, sep ="\n")
import time
import math

valueArea = 0
valuePerimeter= 0
valueRaio = 0, 
valueDiamiter =0
validation = True

while(validation):
    try:
        value = float(input("\nDigite o perímetro de uma circunferência em metros: ").replace(",", "."))
        valuePerimeter = value
        validation = False
    except:
        print("\nValor digitado é invalido, digite novamente")
        time.sleep(2)

valueDiamiter = (valuePerimeter/math.pi)
print(f"\nDiametro: {valueDiamiter:.2f}m")

valueRaio = valueDiamiter/2
print(f"\nRaio: {valueRaio:.2f}m")

valueArea = (math.pow(valueRaio,2))*math.pi
print(f"\nÁrea: {valueArea:.2f}m²")