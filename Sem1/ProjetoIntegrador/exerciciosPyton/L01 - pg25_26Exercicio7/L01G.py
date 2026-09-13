#g)  Ler  quatro  números  inteiros  e  apresentar  o  resultado  da  adição  e  multiplicação,  
# baseando-se  na utilização  do  conceito  da  propriedade  distributiva.
# Ou  seja,  se  forem  lidas  as  variáveis  A,  B,  C,  e  D, 
# devem ser somadas e multiplicadas 
# A com B, A com C e A com D. Depois B com C, B com D e por fim C  com  D.  
# Perceba  que  será  necessário  efetuar  seis  operações  de  adição  e  
# seis  operações  de multiplicação e apresentar doze resultados de saída.
i=0
j=1
total = 0
cont = 1

valores = ["valorA","valorB","valorC","valorD"]

while i < 4:
    try:
        valores[i] = float(input(f"\ndigite o valor  {valores[i]}: ").replace(",","."))
        print(f"\n {valores[i]}")
    except:
        print("valor invalido, digite novamente: ")
        i-=1
    i +=1

i=0
while (i < 4):
    while(j < 4):
        total += valores[i]*valores[j]
        j+=1
    cont = cont + 1 
    i+=1
    j = cont
print(f"valor total: {total}")