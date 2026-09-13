#h) Elaborar um programa que calcule e apresente o volume de uma caixa retangular, 
# por meio da fórmula VOLUME ← COMPRIMENTO * LARGURA * ALTURA.
import time

result = 1

def areaDaBaseCaixa(length, width):
    area = length * width
    return area

def areaDaCaixa(length, width,height):
    area = ((width * height) * 2) + ((width * length) * 2) + ((length * height) * 2)
    return area

def volumeDaCaixa(length,width,height):
    volume = (length * width * height)
    return volume

def askOperation():
    response = str (input("\nDigite: \n" +
            "\n1 - para  calcular área superficial total do cubo: " +
            "\n2 - para  calcular Volume do cubo: " +
            "\n3 - para  calcular área da base do cubo: " +
            "\n0 - para  sair. \n\n"))

    return response[0]


while result != 0: 
    try:
        ask = int (askOperation())
    except:
        ask = -1

    match ask: 
        case 1: 
            length = float (input("Digite o valor do comprimento: ").replace(",", "."))
            height = float (input("Digite o valor da altura: ").replace(",", "."))
            width = float (input("Digite o valor da largura: ").replace(",", "."))

            result = (areaDaCaixa(length, width, height))
            resultText = str (f"\nA àrea da caixa é : {result:.2f}")
            
        case 2: 
            length = float (input("Digite o valor do comprimento: ").replace(",", "."))
            height = float (input("Digite o valor da altura: ").replace(",", "."));
            width = float (input("Digite o valor da largura: ").replace(",", "."));


            result = (volumeDaCaixa(length, width, height));
            resultText = str (f"O volume da caixa é : {result:.2f}")
            
            
        case 3: 
            length = float (input("Digite o valor do comprimento: ").replace(",", "."))
            height = float (input("Digite o valor da altura: ").replace(",", "."))
            width = float (input("Digite o valor da largura: ").replace(",", "."))


            result = (areaDaBaseCaixa(length, width))
            resultText = str (f"\nA àrea da base da caixa é : {result:.2f}")
            
        case 0: 
            resultText = "Obrigado por sua interação! :)"
            result = 0
            
        case _:
            resultText = "Valor inválido, digite novamente"
            result = -1
    print(f"\n{resultText}")
    time.sleep(3)


print("\n"+"**********FIM DO PROGRAMA**********"+"\n")