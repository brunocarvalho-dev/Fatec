#-*-coding:utf-8-*-
import random
import time


poderes = ("DIAMANTE","NAVALHA","TORNADO","LAVA","GELO","MACHADO")

# ==============ABERTURA DO JOGO===============
def abertura(Jogador, Computador):
    
    print("="*50)
    print("🎴    D U E L O   D E   P E D R A ,   P A P E L    🎴")
    print("                 E   T E S O U R A                   ")
    print("="*50)
    time.sleep(1)
    print("\n⚔️  O DUELO VAI COMEÇAR! ⚔️\n")
    time.sleep(1)
    print("="*50)
    print(f"Pontos de vida")
    print(f"\nJogador: {Jogador}")
    print(f"Computador: {Computador}")
    print("="*50)
    time.sleep(2)


# ================= CARTA ATAQUE ==================
def ataque (ataque):
    cartaAtaque = {"PEDRA" : 10,"PAPEL": 10,"TESOURA":10}
    return cartaAtaque[ataque]

# ================= CARTA POTÊNCIA ==================
def poder (poder):
    cartaPotencia = {"DIAMANTE":4,"NAVALHA":2,"TORNADO":7, "LAVA":6, "GELO":5, "MACHADO":3}
    return cartaPotencia[poder]

# ================= JOGADORES VIDA ==================
def vidaJogadores (valor, jogador):
    vida_jogador = jogador - valor
    return vida_jogador

# ================= EXIBIR PLACAR ==================
def exibir_placar(Jogador, Computador):
    print("\n------ PLACAR - RODADA  ------")
    print(f"  VOCÊ:     {Jogador} ponto(s) ")
    print(f"  INIMIGO:  {Computador} ponto(s) ")
    print("-"*35)

# ================= ESCOLHA PLAYER ==================
def escolha_jogador():
    print("Faça sua jogada:")
    print("[ 1 ] 🥌 PEDRA")
    print("[ 2 ] 📄 PAPEL")
    print("[ 3 ] ✂️  TESOURA")
    
    while True:
        opcao = input("\nDigite sua escolha (1 / 2 / 3): ")
        if opcao == "1":
            return "PEDRA"
        elif opcao == "2":
            return "PAPEL"
        elif opcao == "3":
            return "TESOURA"
        else:
            print("❌ Escolha INVÁLIDA! Tente novamente...\n")

def escolha_jogador_poder():
    poder = random.sample(poderes, k=2)
    simbolo_poder = {
            "DIAMANTE":"💎",
            "NAVALHA":"🪒",
            "TORNADO":"🌪️",
            "LAVA":"🌋",
            "GELO":"❄️",
            "MACHADO":"🪓"
        }
    print("Escolha ataque")
    print(f"[ 1 ] {simbolo_poder[poder[0]]} {poder[0]}")
    print(f"[ 2 ] {simbolo_poder[poder[1]]} {poder[1]}")
    while True:
        opcao = input("\nDigite sua escolha (1 / 2): ")
        if opcao == "1":
            return poder[0]
        elif opcao == "2":
            return poder[1]
        else:
            print("❌ Escolha INVÁLIDA! Tente novamente...\n")

# ================== ESCOLHA DO COMPUTADOR ==================
def escolha_Computador_ataque():
    opcoes = ["PEDRA", "PAPEL", "TESOURA"]
    return random.choice(opcoes)

def escolha_Computador_poderes():
    poder = random.choice(poderes)
    return poder

# ================== EXIBIR JOGADAS ==================
def exibir_jogadas(jogador,jogador_poder, computador,computador_poder):
    simbolo = {
        "PEDRA": "🥌",
        "PAPEL": "📄",
        "TESOURA": "✂️"
    }
    simbolo_poder = {
        "DIAMANTE":"💎",
        "NAVALHA":"🪒",
        "TORNADO":"🌪️",
        "LAVA":"🌋",
        "GELO":"❄️",
        "MACHADO":"🪓"
    }
    
    print(f"\n🔮 VOCÊ jogou: {simbolo[jogador]} {jogador} + {simbolo_poder[jogador_poder]} {jogador_poder}")
    time.sleep(0.8)
    print(f"🃏 INIMIGO jogou: {simbolo[computador]} {computador} + {simbolo_poder[computador_poder]} {computador_poder}")
    time.sleep(1)

# ================== PLACAR ==================
def exibir_placar(pontos_jogador, pontos_computador):
    if(pontos_jogador <= 0):
        pontos_jogador = 0
    if(pontos_computador <= 0):
        pontos_computador = 0
    print(f"\n📊 --- PLACAR - RODADA ---")
    print(f"  VOCÊ:     {pontos_jogador} pontos de vida) ")
    print(f"  INIMIGO:  {pontos_computador} pontos de vida")
    print("-"*35)
    time.sleep(2)

# ================== FIM DE JOGO ==================
def resultado_final(pontos_jogador, pontos_Computador):
    print("\n" + "="*50)
    if pontos_jogador > pontos_Computador:
        print("🏆🏆🏆 PARABÉNS! VOCÊ VENCEU O DUELO! 🏆🏆🏆")
        print("         ⭐ VOCÊ É O REI DOS JOGOS! ⭐")
        
    elif pontos_Computador > pontos_jogador:
        print("💀 VOCÊ FOI DERROTADO... TENTE NOVAMENTE! 💀")
        print("         O INIMIGO VENCEU ESTA VEZ...")
    print("="*50)

# ================== VERIFICAR VENCEDOR DA RODADA ===============
def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "EMPATE"
    elif (jogador == "PEDRA" and computador == "TESOURA") or \
         (jogador == "PAPEL" and computador == "PEDRA") or \
         (jogador == "TESOURA" and computador == "PAPEL"):
        return "JOGADOR"
    else:
        return "COMPUTADOR"

# ================== CALCULO ATAQUE ==================
def calculo_taque(escolha_ataque, escolha_poder):
    valor_ataque = ataque(escolha_ataque) * poder(escolha_poder)
    return valor_ataque

# ================== FUNÇÃO PRINCIPAL ==================
def main():
    Jogador = 20
    Computador = 20
    abertura(Jogador, Computador)
    while(Jogador > 0 and Computador > 0):   
        jogada_jogador = escolha_jogador()
        jogada_jogador_poder = escolha_jogador_poder()
        jogada_pc = escolha_Computador_ataque()
        jogada_pc_poder = escolha_Computador_poderes()

            
        exibir_jogadas(jogada_jogador,jogada_jogador_poder, jogada_pc, jogada_pc_poder)
            
        resultado = verificar_vencedor(jogada_jogador, jogada_pc)
        
        if resultado == "JOGADOR":
            jogador_ataque = calculo_taque(jogada_jogador,jogada_jogador_poder)
            Computador = vidaJogadores(jogador_ataque,Computador)
            print("\n✨ VOCÊ VENCEU ESTA RODADA! ✨")
            time.sleep(1.5)

        elif resultado == "COMPUTADOR":
            print("\n💥 O INIMIGO VENCEU ESTA RODADA! 💥")
            pc_ataque = calculo_taque(jogada_pc,jogada_pc_poder)
            Jogador = vidaJogadores(pc_ataque,Jogador)
            time.sleep(1.5)

        elif resultado == "EMPATE":
            jogador_ataque = calculo_taque(jogada_jogador,jogada_jogador_poder)
            pc_ataque = calculo_taque(jogada_pc,jogada_pc_poder)

            if pc_ataque > jogador_ataque:
                dano = pc_ataque - jogador_ataque
                Jogador = vidaJogadores(dano,Jogador)
                print(f"VOCÊ levou um dano de {dano}")
                time.sleep(1.5)
            elif jogador_ataque > pc_ataque:
                dano = jogador_ataque - pc_ataque
                Computador = vidaJogadores(dano,Computador)
                print(f"O INIMIGO levou um dano de {dano}")
                time.sleep(1.5)
            else:
                print("\n🤝 EMPATE! Ninguém pontuou...")
                time.sleep(1.5)
        
        exibir_placar(Jogador, Computador,)
        time.sleep(1)

    resultado_final(Jogador, Computador)
    print("\nObrigado por jogar! 🎴")

# ================== INICIAR O JOGO ==================
if __name__ == "__main__":
    main()
