#-*-coding:utf-8-*-
'''
d. Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem 
dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. Se o valor da 
média for menor que 7, solicitar a nota de exame, somar com o valor da média e obter nova média. 
Se a nova média for maior ou igual a 5, apresentar uma mensagem dizendo que o aluno foi 
aprovado em exame. Se o aluno não foi aprovado, indicar uma mensagem informando esta 
condição. Apresentar com as mensagens o valor da média do aluno, para qualquer condição. 
'''

import time
notas = ["nota1", "nota2", "nota3", "nota4"]
def mediaNotas(notasAluno):
    media = 0
    for nota in notasAluno:
        media += nota
    mediaTotal = media/len(notasAluno)
    return mediaTotal

def aprovacao (nota):
    media = nota
    if media >= 9:
        msg = f"\nAluno(a) Aprovado!!\nSua nota foi {media:.1f}, parabéns pelo seu desempenho!! :)\n"
    elif media >= 7:
        msg = f"\nAluno(a) aprovado!!\nSua nota foi {media:.1f}, atingiu o minino de 7 pontos.\n"
    else:
        print( f"\nAluno(a) ficou para exame!!\nSua nota foi {media:.1f}, não atingiu o minino de 7 pontos! :(\n")
        media = notaExame(True)
        if (float(media)>=5 ):
            msg = f"\nAluno(a) aprovado!!\nSua nota foi {media:.1f}, atingiu o minino de 5 pontos.\n"
        else:
            msg = f"\nAluno(a) REPROVADO!!\nSua nota foi {media:.1f}, não atingiu o minino de 5 pontos! :(\n"
    return msg

def notaExame(validation):
    valid = validation
    while (valid):
        try:
            value = float(input(f"\nDigite o valor da nota do exame: ").replace(",","."))
            if (value>=0 and value<=10):
                notas.append(value)
                valid = False
            else:
                print("\nValor do segundo termo inválido!, digite novamente")
                time.sleep(1)
        except:
            print("\nValor do segundo termo inválido!, digite novamente")
            time.sleep(1)
    return mediaNotas(notas)

def solicitarNotaPrincipal(validation):   
    i = 0
    valid = validation
    for nota in notas:
        while (valid):
            try:
                value = float(input(f"\nDigite o valor da nota {i+1}: ").replace(",","."))
                if (value>=0 and value<=10):
                    notas[i] = value
                    i = i+1
                else:
                    print("\nValor do segundo termo inválido!, digite novamente")
                    time.sleep(1)
            except:
                    print("\nValor do segundo termo inválido!, digite novamente")
                    time.sleep(1)
            if (i == len(notas)):
                valid =  False 


solicitarNotaPrincipal(True)
media = mediaNotas(notas)
msg = aprovacao (media)

print("\nAs notas do aluno foram")
print(*notas, sep="\n")
time.sleep(2)
print("tam - tam - tam - tam\n\n")
time.sleep(2)
print("PREPARADOS ...........\n\n")
time.sleep(2)
print("Soem os tambores..........\n\n")
time.sleep(2)
print("O resultado de um ano de estudos foi ..............\n\n")
#print(f"\nA média do aluno foi: {media}")
time.sleep(2)
print (msg)