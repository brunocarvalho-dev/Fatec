#-*-coding:utf-8-*-

import time, os, math
# ==================== 3 LADOS - TRIANGULO ====================
def triangulo():
    lados = ["LADO 1","LADO 2", "LADO 3"]
    cont = 0
    for i in lados:
        valid = True
        while(valid):
            try:
                lados[cont] = float(input(f"Digite o valor do {i} do Triângulo: ").replace(",","."))
                if lados[cont] > 0 :
                    cont +=1
                    valid = False
                else:
                    print("valor inválido, digite novamente: ")
                    lados[cont] = i
                    time.sleep(1)
            except:
                print("valor inválido, digite novamente: ")
                lados[cont] = i
                time.sleep(1)
    perimetro = lados[0] + lados[1] +lados[2]
    semiperimetro = (perimetro)/2
    area = math.sqrt(semiperimetro*(semiperimetro - lados[0])*(semiperimetro - lados[1])*(semiperimetro - lados[2])) 
    opcao = escolha_operacao()
    if opcao == "PERIMETRO":
        mostrar_resultado (opcao, perimetro)
    elif opcao == "AREA":
        mostrar_resultado(opcao, area)
# ==================== 4 LADOS - QUADRILATERO ====================
#Ecolha Quadrilátero (quadrado, retângulo, losango, trapézio, pentágono)
def escolha_qual_quadrilatero():
    print("="*68)
    print("Escolha qual quadrilatero deseja saber as medidas: \n")
    print("[ 1 ] QUADRADO")
    print("[ 2 ] RETÂNGULO")
    print("[ 3 ] LOSÂNGULO")
    print("[ 4 ] TRAPÉZIO")
    print("[ 5 ] PENTÁGONO")
    print("="*68)
    valid = True
    while (valid):
        opcao = int(input("\nDigite sua escolha (1 / 2 / 3 / 4 / 5): "))
        if opcao == 1:
            quadrado()
            valid = False
        elif opcao == 2:
            retangulo()
            valid = False
        elif opcao == 3:
            losangulo()
            valid = False
        elif opcao == 4:
            trapezio()
            valid = False
        elif opcao == 5:
            pentagono()
            valid = False
        else:
            print("❌ Escolha INVÁLIDA! Tente novamente...\n")
#Quadrilátero (quadrado)
def quadrado():
    print("="*68)
    print("\nOs quatro lados de um quadrado são iguais\n")
    lados = "LADO 1"
    valid = True
    while(valid):
        i = lados
        try:
            valor_temp = float(input(f"Digite o valor do {i} do Quadrado: ").replace(",","."))
            if lados > 0 :
                lados = valor_temp
                valid = False
            else:
                print("valor inválido, digite novamente: ")
                time.sleep(1)
                
        except:
            print("valor inválido, digite novamente: ")
            lados = i
            time.sleep(1)
    print("="*68)
    perimetro = lados*4
    area = math.pow(lados, 2) 
    opcao = escolha_operacao()
    if opcao == "PERIMETRO":
        mostrar_resultado (opcao, perimetro)
    elif opcao == "AREA":
        mostrar_resultado(opcao, area)
#Quadrilátero (retângulo)
def retangulo():
    print("="*68)
    print("Para calcular o Retangulo você precisa de 2 medidas:")
    print("\nLado MAIOR e Lado MENOR")
    print("="*68)
    lados = ["LADO 1", "LADO 2"]
    cont = 0
    for i in lados:
        valid = True
        while(valid):
            try:
                valor_temp = float(input(f"\nDigite o valor do {i} do Retângulo: ").replace(",","."))
                if valor_temp > 0 or (lados[0] != lados[1]):
                    lados[cont] = valor_temp
                    cont +=1
                    valid = False
                else:
                    print("valor inválido, digite novamente: ")
                    time.sleep(1)
            except:
                print("valor inválido, digite novamente: ")
                lados[cont] = i
                time.sleep(1)
    print("="*68)
    perimetro = lados[0]*2 + lados[1]*2
    area = lados[0] * lados[1] 
    opcao = escolha_operacao()
    if opcao == "PERIMETRO":
        mostrar_resultado (opcao, perimetro)
    elif opcao == "AREA":
        mostrar_resultado(opcao, area)
# losangulo main
def losangulo():
    print("="*68)
    print("Para calcular o Losangulo você precisa de 2 medidas:")
    print("Digite: \n")
    print("[ 1 ] DIAGONAL MAIOR X DIAGONAL MENOR")
    print("[ 2 ] DIAGONAL MAIOR X ALTURA")
    while True:
        opcao = input("\nDigite sua escolha (1 / 2 ): ")
        if opcao == "1":
            losangulo_base_base()
        elif opcao == "2":
            losangulo_base_altura()
        else:
            print("❌ Escolha INVÁLIDA! Tente novamente...\n")
#losango (base/altura)
def losangulo_base_altura():
    print("="*68)
    altura = ["DIAGONAL", "ALTURA"]
    cont = 0
    for i in altura:
        valid = True
        while(valid):
            try:
                valor_temp = float(input(f"Digite o valor do {i} do Losângulo: ").replace(",","."))
                if valor_temp > 0 and (altura[0] != altura[1]):
                    altura[cont] = valor_temp
                    cont +=1
                    valid = False
                else:
                    print("valor inválido, digite novamente: ")
                    time.sleep(1)
            except:
                print("valor inválido, digite novamente: ")
                altura[cont] = i
                time.sleep(1)
    perimetro = altura[0]*2 + altura[1]*2
    area = altura[0] * altura[1]
    opcao = escolha_operacao()
    if opcao == "PERIMETRO":
        mostrar_resultado (opcao, perimetro)
    elif opcao == "AREA":
        mostrar_resultado(opcao, area)
#losango (bases)
def losangulo_base_base():
    print("="*68)
    lados = ["DIAGONAL MAIOR", "DIAGONAL MENOR"]
    cont = 0
    for i in lados:
        valid = True
        while(valid):
            try:
                valor_temp = float(input(f"Digite o valor do {i} do Losângulo: ").replace(",","."))
                if valor_temp > 0 and (lados[0] != lados[1]):
                    lados[cont] = valor_temp
                    cont +=1
                    valid = False
                else:
                    print("valor inválido, digite novamente: ")
                    lados[cont] = i
                    time.sleep(1)
            except:
                print("valor inválido, digite novamente: ")
                lados[cont] = i
                time.sleep(1)
    perimetro = lados[0]*2 + lados[1]*2
    area = (lados[0] * lados[1])/2
    opcao = escolha_operacao()
    if opcao == "PERIMETRO":
        mostrar_resultado (opcao, perimetro)
    elif opcao == "AREA":
        mostrar_resultado(opcao, area)
#Quadrilátero (trapézio)
def trapezio():
    print("="*68)
    print("\nO TRAPÉZIO precisa de três medidas: ")
    print("\nBase MAIOR - Base MENOR - ALTURA\n")
    lados = ["BASE MAIOR", "BASE MENOR", "ALTURA"]
    cont = 0
    for i in lados:
        valid = True
        while(valid):
            try:
                valor_temp = float(input(f"Digite o valor do {i} do Trapézio: ").replace(",","."))
                if valor_temp > 0 and (lados[0] != lados[1] != lados[2]):
                    lados[cont] = valor_temp
                    cont +=1
                    valid = False
                else:
                    print("valor inválido, digite novamente: ")
                    time.sleep(1)
            except:
                print("valor inválido, digite novamente: ")
                time.sleep(1)
    perimetro = lados[0]+ lados[1] + 2*(math.sqrt(math.pow(lados[2],2)+math.pow((lados[0] - lados[1]),2)))
    area = ((lados[0] + lados[1])*lados[2])/2
    opcao = escolha_operacao()
    if opcao == "PERIMETRO":
        mostrar_resultado (opcao, perimetro)
    elif opcao == "AREA":
        mostrar_resultado(opcao, area)
# ==================== 5 LADOS - PENTAGONO ====================
def pentagono():
    print("="*68)
    print("\nO Pentâgono tem cinco lados e todos são iguais\n")
    lados = "LADO 1"
    valid = True
    while(valid):
        i = lados
        try:
            lados = float(input(f"Digite o valor do {i} do Pentágono: ").replace(",","."))
            if lados <= 0 :
                print("valor inválido, digite novamente: ")
                lados = i
                time.sleep(1)
            else:
                valid = False
        except:
            print("valor inválido, digite novamente: ")
            lados = i
            time.sleep(1)
    perimetro = lados*5
    area = (5*math.pow(lados, 2))/(4*(math.tan(math.radians(36)))) 
    opcao = escolha_operacao()
    if opcao == "PERIMETRO":
        mostrar_resultado (opcao, perimetro)
    elif opcao == "AREA":
        mostrar_resultado(opcao, area)
# ==================== ESCOLHA PERÍMETRO / ÁREA ====================
def escolha_operacao():
    valid = True
    print("\nPara saber as medidas, Digite:")
    print("[ 1 ] PERÍMETRO")
    print("[ 2 ] ÁREA")
    while (valid):
        opcao = input("\nDigite sua escolha (1 / 2 ): ")
        if opcao == "1":
            valid = False
            return "PERIMETRO"
        elif opcao == "2":
            valid = False
            return "AREA"
        else:
            print("❌ Escolha INVÁLIDA! Tente novamente...\n")
# ==================== MODE ====================
def caunt_size (lados):
    size = lados
    if size < 3:
        print(f"Sua figura geométrica contem {size} lados, \nPortanto: NÃO É UM POLÍGONO")
        time.sleep(2)
        os.system("cls")
        size = 0
        entrada_valores()
    elif size == 3:
        time.sleep(2)
        os.system("cls")
        size = 0
        triangulo()
    elif size == 4:
        time.sleep(2)
        os.system("cls")
        size = 0
        escolha_qual_quadrilatero()
    elif size == 5:
        time.sleep(2)
        os.system("cls")        
        size = 0
        pentagono()
    elif size > 5:
        print("POLÍGONO NÃO IDENTIFICADO!!!\n Só sei contar até 5")
        time.sleep(2)
        os.system("cls")
        size = 0
        entrada_valores()
# ==================== MOSTRAR RESULTADO ==================== 
def mostrar_resultado(opcao , valor):
    print("="*68)
    os.system("cls")
    print("="*68)
    if opcao == "PERIMETRO":
        print(f"\nO {opcao} é: {valor:.1f} metros\n")
    elif opcao == "AREA":
        print(f"\nA {opcao} é: {valor:.1f} m²\n")
    print("="*68)
# ==================== ENTRADA DOS VALORES ====================
def entrada_valores():
    num = 0
    valid = True
    while(valid):
        try:
            num = int(input("\nDigite o núemro de lados tem sua figura geométrica: "))
            valid =False
        except:
            print("VALOR INVÁLIDO!\nDIGITE NOVAMENTE:")
    caunt_size(num)
# ==================== MAIN ====================
def main () :
    os.system("cls")
    print("======================= OLÁ! SEJA BEM VINDO =======================") 
    print("==================== CALCULADORA DE GEOMÊTRIAS ====================\n")  
    print("="*68)
    print("============= QUANTOS LADOS TEM SUA FIGURA GEOMÉTRICA? =============\n")
    print("="*68)
    time.sleep(2)
    entrada_valores()
# ==================== START ====================
if __name__ == "__main__":
    main()

    '''
1. Escreva um programa para ler o número de lados (NumLados) de um polígono regular,
e a medida do lado (MedLado).
-> Se o número de lados for igual a 3 imprima “TRIÂNGULO”, 
calcule e mostre a área do triângulo (Use o Teorema de HERON para calcular a área do triangulo 
somente com lados, pesquise no google).
-> Se o número de lados for igual a 4 imprima “QUADRADO”, 
calcule  e mostre a área do quadrado. 
->Se o número de lados for igual a 5 imprime  “PENTÁGONO”, 
calcule e mostre a área do pentágono. (Pesquise no google com se calcula a área de um PENTAGONO)
-> Acrescente as seguintes mensagens ao exercício 1 conforme o caso.
-> Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
−> Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO. 
'''