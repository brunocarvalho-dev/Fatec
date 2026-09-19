#-*-coding:utf-8-*-
'''
f. Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente. 

'''
import time
valores_digitado = ["Valor de A","Valor de B","Valor de C"]
cont = 0
for i in valores_digitado:
    valid = True
    v_atual = i
    while (valid):
        try:
            valores_digitado[cont] = float(input("Digite o %s: "%(i)).replace(",","."))
            valid = False
            cont+=1
        except:
            print("Valor inválido digite novamente: \n")
            time.sleep(2)
            valores_digitado = v_atual
valores_crescente = valores_digitado
print(valores_digitado)
valores_crescente.sort()
print(valores_crescente)
'''
print(f"Os valores digitados foram:\n")
print(*valores_digitado, sep="; ")
print("\nOs valores Crescentes são:")
print(*valores_crescente, sep="; ")
'''