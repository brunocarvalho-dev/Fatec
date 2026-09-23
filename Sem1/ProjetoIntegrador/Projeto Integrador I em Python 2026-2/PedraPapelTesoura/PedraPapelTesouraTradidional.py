import random
import time

# ================== TELA DE ABERTURA ==================
def abertura():
    
    print("="*50)
    print("🎴    D U E L O   D E   P E D R A ,   P A P E L    🎴")
    print("                 E   T E S O U R A                   ")
    print("="*50)
    time.sleep(1)
    print("\n⚔️  O DUELO VAI COMEÇAR! ⚔️\n")
    time.sleep(1)

# ================== ESCOLHA DO JOGADOR ==================
def escolha_jogador():
    print("Faça sua jogada:")
    print("[ 1 ] 🪨 PEDRA")
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

# ================== ESCOLHA DO COMPUTADOR ==================
def escolha_computador():
    opcoes = ["PEDRA", "PAPEL", "TESOURA"]
    return random.choice(opcoes)

# ================== VERIFICAR VENCEDOR DA RODADA ==================
def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "EMPATE"
    elif (jogador == "PEDRA" and computador == "TESOURA") or \
         (jogador == "PAPEL" and computador == "PEDRA") or \
         (jogador == "TESOURA" and computador == "PAPEL"):
        return "JOGADOR"
    else:
        return "COMPUTADOR"

# ================== EXIBIR JOGADAS ==================
def exibir_jogadas(jogador, computador):
    simbolo = {
        "PEDRA": "🪨",
        "PAPEL": "📄",
        "TESOURA": "✂️"
    }
    
    print(f"\n🔮 VOCÊ jogou: {simbolo[jogador]} {jogador}")
    time.sleep(0.8)
    print(f"🃏 INIMIGO jogou: {simbolo[computador]} {computador}")
    time.sleep(1)

# ================== PLACAR ==================
def exibir_placar(pontos_jogador, pontos_computador, rodada):
    print(f"\n📊 --- PLACAR - RODADA {rodada} ---")
    print(f"  VOCÊ:     {pontos_jogador} ponto(s) ❤️")
    print(f"  INIMIGO:  {pontos_computador} ponto(s) 💔")
    print("-"*35)

# ================== FIM DE JOGO ==================
def resultado_final(pontos_jogador, pontos_computador):
    print("\n" + "="*50)
    if pontos_jogador > pontos_computador:
        print("🏆🏆🏆 PARABÉNS! VOCÊ VENCEU O DUELO! 🏆🏆🏆")
        print("         ⭐ VOCÊ É O REI DOS JOGOS! ⭐")
    elif pontos_computador > pontos_jogador:
        print("💀 VOCÊ FOI DERROTADO... TENTE NOVAMENTE! 💀")
        print("         O INIMIGO VENCEU ESTA VEZ...")
    else:
        print("⚖️ O DUELO TERMINOU EMPATADO! ⚖️")
    print("="*50)

# ================== FUNÇÃO PRINCIPAL ==================
def main():
    abertura()
    
    total_rodadas = int(input("Quantas rodadas terá o duelo? "))
    while total_rodadas <= 0:
        total_rodadas = int(input("Digite um número válido: "))
    
    pontos_jogador = 0
    pontos_computador = 0
    
    for rodada in range(1, total_rodadas + 1):
        print(f"\n{'='*30}")
        print(f"    ⚔️  RODADA {rodada} de {total_rodadas}")
        print(f"{'='*30}")
        
        jogada_jogador = escolha_jogador()
        jogada_pc = escolha_computador()
        
        exibir_jogadas(jogada_jogador, jogada_pc)
        
        resultado = verificar_vencedor(jogada_jogador, jogada_pc)
        
        if resultado == "JOGADOR":
            print("\n✨ VOCÊ VENCEU ESTA RODADA! ✨")
            pontos_jogador += 1
        elif resultado == "COMPUTADOR":
            print("\n💥 O INIMIGO VENCEU ESTA RODADA! 💥")
            pontos_computador += 1
        else:
            print("\n🤝 EMPATE! Ninguém pontuou...")
        
        exibir_placar(pontos_jogador, pontos_computador, rodada)
        time.sleep(1)
    
    resultado_final(pontos_jogador, pontos_computador)
    print("\nObrigado por jogar! 🎴")

# ================== INICIAR O JOGO ==================
if __name__ == "__main__":
    main()