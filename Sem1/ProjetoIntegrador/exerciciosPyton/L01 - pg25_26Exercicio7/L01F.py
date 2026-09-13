#f) Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B, 
# e efetuar a troca dos valores de forma que a variável A passe a possuir o valor da variável B ,
# e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados

valorA = str(input("Digite o valor da variavél A: "))
valorB = str(input("Digite o valor da variavél B: "))

intermediario = valorB
valorB = valorA
valorA = intermediario


print(f"\nO valor de A é: {valorA}\n")
print(f"\nOvalor de B é: {valorB}\n")         

