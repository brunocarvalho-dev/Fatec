#-*-coding:utf-8-*-
'''
Formula: IMC = peso / altura * altura
IMC menor que 18,5 exibir "abaixo do peso"
IMC entre 18,5 e 24,9 exibir "Peso normal"
IMC maior que 25 exibir está com sobrepeso
'''

import os
import sys
import math
import time

os.system ("cls")

def indiceIMC(imc):
    if (imc>=25):
        msg = "IMC maior que 25 , você está com sobrepeso, PRECISA FAZER EXECÌCIOS"
    elif(imc>=18.5):
        msg = "IMC entre 18,5 e 24,9, você está com o Peso normal, PARABÉNS!!!"
    else:
        msg = "IMC menor que 18,5, você está abaixo do peso, PRECISA SE ALIMENTAR MELHOR"
    return msg

def calculoIMC (peso, altura):
    imc = peso /math.pow(altura, 2)
    return float (imc)

def pesoIdeal(altura):
    pesoIdeal = 21.75*math.pow(altura,2)
    msg = str (f"\nSeu peso ideal é {pesoIdeal:.2f}")
    return msg
    
nome = input("Digite  seu nome: ").title()
peso = float (input("Digite seu peso: ").replace(",","."))
altura = float (input("Digite sua altura: ").replace(",","."))

imc  = calculoIMC(peso, altura)
msg = indiceIMC (imc)

print(f"\n{nome}, {msg}.\nO valor do seum IMC é {imc:.2f}")
time.sleep(3)
print(pesoIdeal(altura))

os.system("pause")



