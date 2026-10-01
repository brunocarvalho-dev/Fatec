#-*-coding:utf-8-*-
import time, os, math
raiz = ["X1","X2"]
eq_segundo_grau = ["a", "b", "c"]
valor_delta = "DELTA"
# ====================== LEITURA =======================    
def entrada_de_valores():
    cont = 0
    print("\nEQUAÇÃO => a.X² + b.X + c\n")
    for i in eq_segundo_grau:
        while True:
            if cont == 4:
                print("NÚMERO DE TENTATIVAS EXCEDIDAS")
                time.sleep(2)
                menu()
            try:
                eq_segundo_grau[eq_segundo_grau.index(i)] = float(input(f"DIGITE O VALOR DE {i}: ").replace(",","."))
                break
            except:
                print("VALOR INVÁLIDO, DIGITE NOVAMENTE!")
                cont +=1
    delta()            
# ======================= RAIZES =======================
def bhaskara(delta):
    raiz[raiz.index("X1")] = (-(eq_segundo_grau[1]) + math.sqrt(delta))/2*eq_segundo_grau[0]
    raiz[raiz.index("X2")] = (-(eq_segundo_grau[1]) - math.sqrt(delta))/2*eq_segundo_grau[0]
    mostrar_valor()
# ======================= DELTA =======================
def delta():
    if eq_segundo_grau[0] == "a" or eq_segundo_grau[1] == "b" or eq_segundo_grau[2] == "c":
        print("\nVALORES NÃO INSERIDOS, FAVOR INSIRA OS VALORES DA EQUAÇÃO!")
        time.sleep(1.5)
        entrada_de_valores()
    else:
        valor_delta = math.pow(eq_segundo_grau[1],2) - 4 * eq_segundo_grau[0] * eq_segundo_grau[2]
    if valor_delta >= 0:
        mostrar_valor(msg = (f"o valor de DELTA é {valor_delta}\nSem solução no conjunto dos númerosReais!"))
        time.sleep(2)
        menu()
    else:
        bhaskara(valor_delta)
# ================= SAÍDA DE VALORES =================
def mostrar_valor(msg=""):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*68)
    print("# ====================== RESPOSTA DE BHASKARA ====================== #")
    print(f"\nO valor de \"a\" = {eq_segundo_grau[0]}")
    print(f"\nO valor de \"b\" = {eq_segundo_grau[1]}")
    print(f"\nO valor de \"c\" = {eq_segundo_grau[2]}")
    print(f"\nO valor de DELTA = {valor_delta}")
    print("="*68)
    if msg != "":
        print(f"\n{msg}")
    else:
        print(f"\nAs raizes da equação de segundo grau são:\n")
        print(f"# ===== A Raiz de X'¹ = {raiz[0]}")
        print(f"# ===== A Raiz de X'² = {raiz[1]}\n")
    print("="*68)
    time.sleep(3)
    os.system("pause")
    raiz = ["X1","X2"]
    eq_segundo_grau = ["a", "b", "c"]
    valor_delta = "DELTA"
    menu()
# ================= MENU =================
def menu():
    valid = True
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n# ============================= MENU ============================= #")
    print("="*68)
    print(" [ 1 ] ========== Leitura")
    print(" [ 2 ] ========== Cálculo")
    print(" [ 3 ] ========== Impressão")
    print(" [ 0 ] ========== Saída \n")
    print("="*68)
    while valid:
        try:
            opcao_menu = int (input("\nDIGITE A OPÇÃO DO MENU: "))
            if opcao_menu == 0:
                print("\nOBRIGADO POR UTILIZAR NOSSO SISTEMA!")
                valid = False
                os.abort()
            elif opcao_menu == 1:
                valid = False
                entrada_de_valores()
            elif opcao_menu == 2:
                valid = False
                delta()
            elif opcao_menu == 3:
                valid = False
                mostrar_valor()
            else:
                print("\nOPÇÃO INVÁLIDA! DIGITE NOVAMENTE!")
        except:
            print("\nOPÇÃO INVÁLIDA! DIGITE NOVAMENTE!")      
# ==================== MAIN ====================
def main () :
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================== OLÁ! SEJA BEM VINDO =======================\n") 
    print("============== CALCULADORA DE EQUAÇÃO DE SEGUNDO GRAU ==============")  
    print("="*68)
    time.sleep(3)
    menu()
# ======================= START =======================
if __name__=="__main__":
    main()
'''
Faça o quadro resumo, código fonte e o diagrama de blocos com menu (IF ELSE)
de um programa para ler os coeficientes A (A diferente de 0) , B, C de uma equação
do segundo grau; Calcular o Delta = B * B - 4 * A * C; SE o Delta for positivo calcule
também as raízes X1 = -b + raiz(delta)/2*a , x2 = -b - raiz (delta) / 2*a, SENÃO SE
o Delta for negativo, mostre a mensagem “Sem solução no conjunto dos números
Reais!”; Ao final mostre A,B,C e Delta na tela; SE Delta for maior ou igual a zero,
mostre X1 e X2 também; (Faça um menu com as opções necessário, leitura,
cálculo, impressão e saída)

'''