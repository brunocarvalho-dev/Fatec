#-*-coding:utf-8-*-
'''
e. Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo da equação completa de 
segundo grau, apresentando as duas raízes, se para os valores informados for possível efetuar o 
referido cálculo. Lembre-se de que a variável A deve ser diferente de zero. 
'''
import time
import math
raiz = {"x1": 0, "x2": 0}
quadraticEquationValues = ["valueA", "valueB", "valueC"]
validation = True

def baskara (valueA, valueB, valueC):
    a = valueA
    b = valueB
    c = valueC

    delta = (math.pow(b,2) - 4 * a * c)

    raiz ["x1"] = ((-1*(b) + math.sqrt(delta)) / (2*a))
    raiz ["x2"] = ((-1*(b) - math.sqrt(delta)) / (2*a))

    return raiz

def quadraticEquation():
    i = 0
    valid = True
    for v in quadraticEquationValues:
        while(valid):
            try:
                quadraticEquationValues[i] = float (input(f"\ndigite o valor de {quadraticEquationValues[i]}: ").replace(",","."))
                if ((quadraticEquationValues[0] != 0 and quadraticEquationValues[i] != "valueA" and quadraticEquationValues[i] != "valueB" and quadraticEquationValues[i] != "valueC") ):                   
                    i= i+1
                elif(quadraticEquationValues[0] == 0):
                    print("\nA não pode ser igual a 0:")
                    quadraticEquationValues[0] = "valueA"
                    time.saleep(1)
                else:
                    print("\nValor invalido! Digite novamente:")
                    time.sleep(1)   
            except:
                print("\nValor invalido! Digite novamente:")
                time.sleep(1)
            if (i == len(quadraticEquationValues)):
                valid =  False 

quadraticEquation()
baskara(quadraticEquationValues[0], quadraticEquationValues[1], quadraticEquationValues[2])

for x in raiz:
    print(f"\nRaiz {x} : {raiz.get(x)}")

"""
print(f"\n{raiz.get(x)}") # saida - 0.2
print(f"\n{raiz.values()}") # saida dict_values([0.0, -0.2])
print(f"\n{dict(raiz)}") # saida  {'x1': 0.0, 'x2': -0.2}
print(f"\nAs riazes de deta são\n{raiz.items()}\n".replace("dict_items","\n")) # saiida As riazes de deta são ([('x1', 0.0), ('x2', -0.2)])
"""