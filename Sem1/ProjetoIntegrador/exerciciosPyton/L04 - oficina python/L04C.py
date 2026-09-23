#-*-coding:utf-8-*-
'''
3. Escreva um programa que leia o valor de 3 lados inteiros positivos (A,B e C) de um triângulo. 
-> No início do programa compare os lados para saber se é uma figura de três lados apenas 
ou se é um triângulo, Se qualquer um dos lados for maior ou igual a soma dos outros dois 
então a figura não é um triângulo.  SE ( A >= (B+ C) ou B >=(A+C) ou C >= (B+A)   ). Se for um triangulo, descubra o TIPO de triângulo: “equilátero”, “escaleno” ou “isósceles”. Imprima ao final o TIPO de triângulo. 
-> Verifique na internet para saber como identificar o TIPO de triângulo. 
'''
import time, os
# ==================== MOSTRAR RESULTADO ==================== 
def mostrar_resultado(opcao):
    os.system("cls")
    print("="*68)
    print(f"\nA figura {opcao}\n")
    print("="*68)
# ==================== ENTRADA DOS VALORES ====================
def entrada_valores():
    lados = ["LADO A","LADO B","LADO C"]
    cont = 0
    print("\nVamos saber se é apenas uma figura de três lados, se é um TRIÂNGULO")
    print("Se qualquer um dos lados for maior ou igual a soma dos outros doiS, \nentão a figura não é um triângulo\n")
    print("="*68)
    for i in lados:
        valid = True
        while(valid):
            try:
                num_temp = int(input(f"\nDigite o valor do {i} da sua figura geométrica: "))
                if (num_temp > 0):
                    lados[cont] = num_temp
                    cont += 1
                    valid = False
            except:
                print("VALOR INVÁLIDO!\nDIGITE NOVAMENTE:")
                time.sleep(1)
    validacao_triangulo(lados)

# ==================== MODE ====================
def validacao_triangulo(lados):
    if lados[0] >= (lados[1] + lados[2]) or lados[1] >= (lados[0] + lados[2] or lados[2] >= (lados[0] + lados[1])):
        mostrar_resultado("não é um TRIÂNGULO")
    elif(lados[0] == lados[1] == lados[2]):
        mostrar_resultado("é um TRIÂNGULO EQUILÁTERO")
    elif(lados[0] == lados[1] != lados[2] or lados[0] == lados[2] != lados[1] or lados[1] == lados[2] != lados[0]):
        mostrar_resultado("é um TRIÂNGULO ISÓCELES" )
    elif(lados[0] != lados[1] != lados[2]):
        mostrar_resultado("é um TRIÂNGULO ESCALENO")

# ==================== MAIN ====================
def main () :
    os.system("cls")
    print("======================= OLÁ! SEJA BEM VINDO =======================") 
    print("==================== CALCULADORA DE TRIÂNGULOS ====================\n")  
    print("="*68)
    print("=========== VAMOS DESCOBRIR SE SUA FIGURA É UM TRINGULO? ==========\n")
    print("="*68)
    time.sleep(2)
    entrada_valores()
# ==================== START ====================
if __name__ == "__main__":
    main()