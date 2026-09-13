#-*-coding:utf-8-*-
#a. Ler dois valores numéricos inteiros e 
#apresentar o resultado da diferença do maior pelo menor valor. 
value1 = 0
value2 = 0

def highestValue (value1, value2):
    if(value1 > value2):
        total = value1 - value2
    else:
        total = value2 - value1
        return total

validation = True    

while (validation):
    try:
        value1 = float(input("\nDigite o valor do primeiro termo: ").replace(",","."))
        while (validation):
            try:
                value2 = float(input("\nDigite o valor do segundo termo: ").replace(",","."))
                validation =  False
            except:
                    print("\nValor do segundo termo inválido!, digite novamente")
    except:
        print("\nValor do primeiro termo inválido!, digite novamente")
total = highestValue(value1,value2)
print(f"\n\nA diferença entre {value1:.0f} e {value2:.0f} é {total:.0f}")