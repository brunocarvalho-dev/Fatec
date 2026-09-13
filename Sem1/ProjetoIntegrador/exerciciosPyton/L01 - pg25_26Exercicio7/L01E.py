#e)Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, 
# utilizando a fórmula PRESTACAO ← VALOR + (VALOR * TAXA/100) * TEMPO).

def calculo_prestacao(valor, taxa):
    total = valor + (valor * (taxa/100))
    return total
    
def verificacao_valor(valor):
    if valor <= 0:
        valor = False
    else:
        valor = True
    return valor

validation = False

while validation:
    try:
        valor = float(input("\nDigite o total do veiculo: ").replace(",","."))
    except:
        validation = verificacao_valor(valor)
        print("valor invalido, digite novamente: ")

validation = False
while validation ==False:
    taxa = float(input("\ndigite o valor da taxa em porcentagem (%): ").replace(",","."))
    validation = verificacao_valor(taxa)
    if validation == False:
        print("valor invalido, digite novamente: ")

prestacao = (calculo_prestacao(valor, taxa))

print(f"\nOvalor da prestação atualizada é: R${prestacao:.2f}")

