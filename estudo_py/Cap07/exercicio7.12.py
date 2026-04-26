# 1. Crie um tabuleiro usando uma lista de 3 elementos, onde cada elemento é uma lista de 3 elementos.
# 2. O jogo deve alternar entre dois jogadores (X e O).
# 3. O usuário escolhe a posição usando o teclado numérico (1 a 9).
# 4. Verifique se a posição está livre antes de marcar.
# 5. A cada jogada, verifique se alguém venceu (linhas, colunas ou diagonais).
# DICA DE MAPEAMENTO (Teclado Numérico):
# 7 | 8 | 9
# ---------
# 4 | 5 | 6
# ---------
# 1 | 2 | 3
topo = ["7", "8", "9"]
meio = ["4", "5", "6"]
baixo = ["1", "2", "3"]
tabuleiro = [topo, meio, baixo]

jogador = "X"
jogadas_totais = 0

while True:
    # 2. Desenho do Tabuleiro
    print(f"\n {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
    print("-----------")
    print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
    print("-----------")
    print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} \n")

    jogada_valida = False
    
    # 3. Entrada de dados
    escolha = int(input(f"Vez do {jogador}. Escolha (1-9): "))

    # 4. Os 9 IFs de Posição
    if escolha == 7:
        if tabuleiro[0][0] == "7":
            tabuleiro[0][0] = jogador
            jogada_valida = True
    elif escolha == 8:
        if tabuleiro[0][1] == "8":
            tabuleiro[0][1] = jogador
            jogada_valida = True
    elif escolha == 9:
        if tabuleiro[0][2] == "9":
            tabuleiro[0][2] = jogador
            jogada_valida = True
    elif escolha == 4:
        if tabuleiro[1][0] == "4":
            tabuleiro[1][0] = jogador
            jogada_valida = True
    elif escolha == 5:
        if tabuleiro[1][1] == "5":
            tabuleiro[1][1] = jogador
            jogada_valida = True
    elif escolha == 6:
        if tabuleiro[1][2] == "6":
            tabuleiro[1][2] = jogador
            jogada_valida = True
    elif escolha == 1:
        if tabuleiro[2][0] == "1":
            tabuleiro[2][0] = jogador
            jogada_valida = True
    elif escolha == 2:
        if tabuleiro[2][1] == "2":
            tabuleiro[2][1] = jogador
            jogada_valida = True
    elif escolha == 3:
        if tabuleiro[2][2] == "3":
            tabuleiro[2][2] = jogador
            jogada_valida = True

    # 5. Verificação de Vitória
    venceu = False
    
    # Linhas
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]: venceu = True
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]: venceu = True
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]: venceu = True
    # Colunas
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]: venceu = True
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]: venceu = True
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]: venceu = True
    # Diagonais
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]: venceu = True
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]: venceu = True

    if venceu:
        # Imprime o tabuleiro uma última vez para mostrar o lance final
        print(f"\n {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} ")
        print("-----------")
        print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} ")
        print("-----------")
        print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} ")
        print(f"\nPARABÉNS! O JOGADOR {jogador} VENCEU!")
        break

    # 6. Verificação de Empate e Troca de Jogador
    if jogada_valida:
        jogadas_totais += 1
        
        if jogadas_totais == 9:
            print("\nDEU VELHA!")
            break
            
        # Troca o jogador
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"
    else:
        print("\nJogada inválida! Tente novamente.")

    
    