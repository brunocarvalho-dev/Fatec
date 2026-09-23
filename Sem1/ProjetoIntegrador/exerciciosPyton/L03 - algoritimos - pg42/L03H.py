#-*-coding-8-*-
'''
h. Efetuar a leitura de cinco números inteiros e identificar o maior e o menor valores. 
'''
import time, os
# ==================== VARIAVEIS GLOBAL ====================
num_int = ["Número 1","Número 2","Número 3","Número 4","Número 5"]

# ==================== MAIN ==================== 
def main ():
    os.system("cls")
    i = 0
    valid = True
    for num in num_int:
        while(valid):
            try:
                num_int[i] = int(input(f"\nDigite o valor do {num}"))
                i += 1
                valid = False
            except:
                print("Valor inválido! Digite novamente: ")
    mostra_resultado()

# ==================== IMPRIME RESULTADO ==================== 
def mostra_resultado():
    print
# ==================== START ==================== 
if __name__ == "__main__":
    main()