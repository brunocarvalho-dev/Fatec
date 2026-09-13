#d)    Efetuar  o  cálculo  da  quantidade  de  litros  de  combustível  gasta    em  uma  viagem,  
# utilizando  um automóvel  que  faz  12  Km  por  litro.
#Para  obter  o  cálculo,  o  usuário  deve  fornecer  ,
# o  tempo  gasto (TEMPO) e a velocidade  média (VELOCIDADE) durante  a viagem.
#Desta forma, será possível obter a distância  percorrida  com  a  
# fórmula  DISTANCIA ←  TEMPO  *  VELOCIDADE.  Possuindo  o  valor  da distância,  
# basta  calcular  a  quantidade  de  litros  de  combustível  utilizada  na  viagem  
# com  a  fórmula LITROS_USADOS ← DISTANCIA / 12.
#Ao final, o programa deve apresentar os valores da velocidade média  (VELOCIDADE),  
# tempo  gasto  na  viagem  (TEMPO),  
# a  distancia  percorrida  (DISTANCIA)  e  a quantidade de litros (LITROS_USADOS) utilizada na viagem
import time
def testeValidador(teste):
    if(teste > 0):
        teste = False
    else:
        teste = True

    return teste
def distanciaViagem(velocidade, tempo):
    distancia = velocidade*tempo
    return distancia

def conveter_tempo(tempo):
    hora = int(tempo)
    minutos = int((tempo - hora)*60)
    return minutos 

def consumo_combustivel():
    consumo = distancia/12
    return consumo

validador = True
while validador:
    try:
        velocidade = (input('Digite a velocidade média da viagem em km/h: ').replace(",","."))
        validador = testeValidador(float (velocidade))
        velocidade = float(velocidade)
    except:
        print("\nValor inválido digite novamente")
        time.sleep(2)

validador = True
while validador:
    try:
        tempo = (input('Digite o tempo gasto na viagem em horas: ').replace(",","."))
        validador = testeValidador(float (tempo))
        tempo = float(tempo)
    except:
        print("\nValor inválido digite novamente")
        time.sleep(2)

horas = int(tempo)
distancia = distanciaViagem(velocidade,tempo)
minutos = conveter_tempo(tempo)
litros_gasto = float(consumo_combustivel())

#teste com {} e {}
resposta = str(f"\nvelocidade média da viagem {velocidade:.2f}km/h")
resposta += str(f"\nO tempo  gasto  na  viagem  foi de {horas} horas e {minutos} minutos,")
resposta += str(f"\nA distancia percorrida foi {distancia:.2f}km/h,")
resposta += str(f"\nA quantidade de {litros_gasto:.1f} litros utilizada na viagem.\n")
print(resposta)




    