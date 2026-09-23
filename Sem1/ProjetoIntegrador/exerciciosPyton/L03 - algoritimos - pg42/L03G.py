#-*-coding:utf-8-*-
'''
g. Efetuar a leitura de quatro números inteiros e apresentar os números que são divisíveis por 2 e 3. 
'''
import time, os
num_int = ["Numero 1","Numero 2","Numero 3","Numero 4",]
# =================== MAIN ===================
def main ():
    os.system("cls")
    i = 0
    for num in num_int:
        valid = True
        while(valid):
            try:
                num_int[i] = int (input("\nDigite o valor do %s: "%num))
                i += 1
                valid = False
            except:
                print("\nValor inválido, digite novamente: ")
                i -= 1
                time.sleep(2)
    mostrar_resultado()

# =================== MOSTRAR RESULTAD ===================
def mostrar_resultado():
    os.system('cls' if os.name == 'nt' else 'clear')
    num_divisivel_2 = []
    num_divisivel_3 = []

    for num in num_int:
        if num %2 == 0:
            num_divisivel_2.append(f"\nO VALOR {num} É DIVISÍVEL POR 2")
        else:
            num_divisivel_2.append(f"\nO VALOR {num} NÃO É DIVISÍVEL POR 2")
        if num %3 == 0:
            num_divisivel_3.append(f"\nO VALOR {num} É DIVISÍVEL POR 3")
        else:
            num_divisivel_3.append(f"\nO VALOR {num} NÃO É DIVISÍVEL POR 3")

    print("="*50)
    print(*num_divisivel_2, sep="\n")
    time.sleep(1)
    print("="*50)
    print(*num_divisivel_3, sep="\n")
    print("\n"+("="*50))
    time.sleep(2)

# =================== START ===================
if __name__ == "__main__":
    main()
#os._exit