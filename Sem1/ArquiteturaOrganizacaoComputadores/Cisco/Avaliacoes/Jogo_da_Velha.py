from random import randrange as rd
import time, os



board = [[1,2,3],[4,"X",6],[7,8,9]]
jogador = ""
computador = ""
# ======================= MOSTA TABULEIRO =======================
def display_board(board):
# A função aceita um parâmetro contendo o status atual da placa
# e o imprime no console.

    
    os.system("cls")
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print(f"|       |       |       |")
    print(f"+-------+-------+-------+")
# ======================= JOGADA USUARIO =======================
def enter_move(board):
# A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
# verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
    valid = True
    display_board(board)
    make_list_of_free_fields(board)
    while(valid):
        escolha = int(input("Digite seu movimento: "))
        if escolha<1 or escolha>9:
            print("JOGADA INVÁLIDA, TENTE NOVAMENTE")
        else:
            jogada = escolha - 1
            row, column = jogada // 3, jogada % 3
            if board[row][column] in ["X","O"]:
                print("JOGADA INVÁLIDA, POSIÇÃO!")
                make_list_of_free_fields(board)
            else:
                board[row][column] = "O"
                valid =False
                draw_move(board)          
# ======= MOSTA JOGADAS POSSIVEIS =======================
def make_list_of_free_fields(board):
 # A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
 # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
    cont = 0
    for i in board:
        for j in i:
            if j != "O" and j != "X":
                cont = cont + 1
    if cont == 0:
        painel_vitoria(board, "VELHA")

# ======================= VERIFICA VITÓRIAS =======================
def victory_for(board):
 # A função analisa o estado da placa a fim de verificar se 
 # o jogador usando 'O's ou 'X's ganhou o jogo
    cont = 0
    for i in board:
        for j in i:
            if j == ["X", "O"]:
                cont +=1
    for i in range(3):
        if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            painel_vitoria(board, "JOGADOR")
            return True
        elif board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            painel_vitoria(board, "COMPUTADOR")
            return True
    for i in range(3):
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            painel_vitoria(board, "JOGADOR")
            return True
        elif board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            painel_vitoria(board, "COMPUTADOR")
            return True
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        painel_vitoria(board, "JOGADOR")
        return True
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        painel_vitoria(board, "COMPUTADOR")
        return True
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        painel_vitoria(board, "JOGADOR")
        return True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        painel_vitoria(board, "COMPUTADOR")
        return True
    else:
        False
# ======================= MOSTA PAINEL VITORIA =======================
def painel_vitoria(board, ganhador):
    os.system("cls")
    print("\n" + "="*50)
    display_board(board)
    print("\n" + "="*50)
    if ganhador == "VELHA":
        print("      INFALIZMENTE NINGUEM VENCEU O DUELO! ")
        print("  ⭐ TENTE NOVAMENTE, QUEM SABE NA PRÓXIMA ⭐")
    if ganhador == "JOGADOR":
        print("🏆🏆🏆 PARABÉNS! VOCÊ VENCEU O DUELO! 🏆🏆🏆")
        print("         ⭐ VOCÊ É O REI DOS JOGOS! ⭐")
            
    elif ganhador == "COMPUTADOR":
        print("💀 VOCÊ FOI DERROTADO... TENTE NOVAMENTE! 💀")
        print("         O INIMIGO VENCEU ESTA VEZ...")
    os.sys.exit()
# ======================= MOVIMENTO COMPUTADOR =======================
def draw_move(board):
 # A função desenha o movimento do computador e atualiza o tabuleiro.
    valid =True
    make_list_of_free_fields(board)
    while(valid):
        row = rd(3)
        column = rd(3)       
        if board [row][column] != "X" and board [row][column] != "O":
            board [row][column] = "X"
            valid = False
# ======================= MAIN =======================
def main(board):
    abertura()
    for i in range (5):
        if victory_for(board):
            break
        else:
            enter_move(board)
# ======================= ABERTURA =======================
def abertura():
    print("="*50)
    print("🎴                 D U E L O                 🎴")
    print("               JOGO   DA   VELHO                ")
    print("="*50)
    time.sleep(1)
    print("\n⚔️          O DUELO VAI COMEÇAR!         ⚔️\n")
    print("="*50)
    print("\nO COMPUTADOR COMEÇA A PRIMEIRA JOGADA")
    time.sleep(2)
# ======================= START =======================

if __name__ == "__main__":
    main(board)
