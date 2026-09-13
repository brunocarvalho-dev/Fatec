#-*-coding:utf-8-*-
"""
b. Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número lido como sendo um 
valor positivo, ou seja, o programa deverá apresentar o módulo de um número fornecido. Lembre-se 
de verificar se o número fornecido é menor que zero; sendo, multiplique-o por -1. 
"""
validation = True
value1 = 0
valueModel = 0

def makePositiveNumber(value):
    positiveNumber = value
    if (value < 0):
        positiveNumber = value * (-1)
    return positiveNumber

while (validation):
            try:
                value1 = float(input("\nDigite o valor do termo: ").replace(",","."))
                valueModel = makePositiveNumber(value1)
                validation =  False
            except:
                    print("\nValor do termo inválido!, digite novamente")

print(f"\nO modulo do número {value1:.1f} é {valueModel:.1f}")