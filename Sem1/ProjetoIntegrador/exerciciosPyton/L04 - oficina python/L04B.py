#-*-coding:utf-8-*-
'''
2. Escreva um programa para ler 3 valores inteiros e escrever o maior deles. 
Considere que o usuário não informará valores iguais, valores nulos ou valores negativos. 
'''
import os
valor_inteiro = ["VALOR 1","VALOR 2","VALOR 3"]
def main():
    os.system("cls")
    cont = 0
    for i in valor_inteiro:
        valid = True
        while(valid):
            try:
                valor_inteiro[cont] = float(input(f"\nDigite o {i} ").replace(",","."))
                if valor_inteiro[cont] > 0 and (valor_inteiro[0] != valor_inteiro[1] != valor_inteiro[2]):
                    cont +=1
                    valid = False
                else:
                    valor_inteiro[cont] = i
            except:
                print("\nValor inválido, Digite novamente")
    mostrar_resultado()
def mostrar_resultado():
    print("="*50)
    print("Os valores digitados em ordem são: ")
    valor_inteiro.sort()
    print(valor_inteiro)
    print("="*50)
    print("O maior valor digitado é: ")
    print(max(valor_inteiro))
    print("="*50)
    print("O menor valor digitado é: ")
    print(min(valor_inteiro))
# ==================== START ====================
if __name__ == "__main__":
    main()