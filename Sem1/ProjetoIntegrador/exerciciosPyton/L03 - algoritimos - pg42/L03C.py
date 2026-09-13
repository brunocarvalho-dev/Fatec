#-*-coding:utf-8-*-
'''
c. Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem 
dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 5. Se o aluno não 
foi aprovado, indicar uma mensagem informando esta condição. Apresentar junto das mensagens o 
valor da média do aluno para qualquer condição. 
'''
import time
validation = True
i = 0
notas = ["nota1", "nota2", "nota3", "nota4"]
def mediaNotas(notasAluno):
    media = 0
    for nota in notasAluno:
        media += nota
    mediaTotal = media/len(notasAluno)
    return mediaTotal

def aprovacao (nota):
    media = nota
    if media < 5:
        msg = f"\nAluno(a) reprovado!!\nSua nota foi {media:.1f}, não atingiu o minino de 5 pontos! :(\n"
    elif media <9:
        msg = f"\nAluno(a) aprovado!!\nSua nota foi {media:.1f}, atingiu o minino de 5 pontos.\n"
    else:
        msg = f"\nAluno(a) Aprovado!!\nSua nota foi {media:.1f}, parabéns pelo seu desempenho!! :)\n"

    return msg

for nota in notas:
    while (validation):
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
            validation =  False 

media = mediaNotas(notas)
print("\nAs notas do aluno foram")
print(*notas, sep="\n")
time.sleep(2)
#print(f"\nA média do aluno foi: {media}")
print (aprovacao(media))