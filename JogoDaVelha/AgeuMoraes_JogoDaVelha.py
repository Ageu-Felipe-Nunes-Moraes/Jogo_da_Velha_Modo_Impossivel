import pygame  # Desenvolvimento de jogos
import os  # Sistema operacional


# inicia a biblioteca do pygame
pygame.init()

# Trazendo arquivos para o jogo através dos seus caminhos relativos
caminho_atual = os.path.abspath(os.path.dirname(__file__))

caminho_relativo_x = os.path.join(caminho_atual, 'xBranco.png')
caminho_relativo_bola = os.path.join(caminho_atual, 'bolaBranca.png')
caminho_relativo_fundo = os.path.join(caminho_atual, 'imagemFundoJogoVelha.jpg')
caminho_relativo_musica = os.path.join(caminho_atual, 'sigma.mp3')

x_imgem = pygame.image.load(caminho_relativo_x)
bola_imagem = pygame.image.load(caminho_relativo_bola)
imagem_fundo = pygame.image.load(caminho_relativo_fundo)
pygame.mixer.music.load(caminho_relativo_musica)
pygame.mixer.music.play(loops=-1)

# Variável boleana para a janela
janela_aberta = True

# Dimensões de tela
largura = 1300
altura = 700

# Configurações de tela
tela = pygame.display.set_mode((largura, altura))
tela.fill((5, 5, 5))
tela.blit(imagem_fundo, (345, 45))
pygame.display.set_caption("JOGO DA VELHA")

# Área de cliqu do jogador
espaco_clique1 = pygame.Rect(365, 60, 185, 185)
espaco_clique2 = pygame.Rect(560, 60, 180, 185)
espaco_clique3 = pygame.Rect(753, 60, 185, 185)
espaco_clique4 = pygame.Rect(365, 255, 185, 180)
espaco_clique5 = pygame.Rect(560, 255, 180, 180)
espaco_clique6 = pygame.Rect(753, 255, 185, 180)
espaco_clique7 = pygame.Rect(365, 447, 185, 185)
espaco_clique8 = pygame.Rect(560, 447, 180, 185)
espaco_clique9 = pygame.Rect(753, 447, 185, 185)

# Variávies boleanas que posicionam e definem o jogo na tela e notifica o ganhador ou perdedor
jogador = False
computador = False

vitoria_humana = False
vitoria_maquina = False
empate = False

x1 = False
x2 = False
x3 = False
x4 = False
x5 = False
x6 = False
x7 = False
x8 = False
x9 = False

b1 = False
b2 = False
b3 = False
b4 = False
b5 = False
b6 = False
b7 = False
b8 = False
b9 = False

clicavel1 = True
clicavel2 = True
clicavel3 = True
clicavel4 = True
clicavel5 = True
clicavel6 = True
clicavel7 = True
clicavel8 = True
clicavel9 = True

defender = True

# Contadores de pontuação
contador_x = 0
contador_bola = 0
contador_empate = 0


# Define as posições de mensagens
def posicoes(mensagem, x, y):
    tela.blit(mensagem, (x, y))


# Reinicia o jogo
def reiniciar():
    global jogador, computador, vitoria_humana, vitoria_maquina, clicavel1, clicavel2, clicavel3, clicavel4, clicavel5,\
        clicavel6, clicavel7, clicavel8, clicavel9, x1, x2, x3, x4, x5, x6, x7, x8, x9, b1, b2, b3, b4, b5, b6, b7, b8,\
        b9, defender, contador_empate, contador_x, contador_bola, empate

    if vitoria_maquina:
        contador_bola += 1

    elif empate:
        contador_empate += 1

    elif vitoria_humana:
        contador_x += 1

    vitoria_humana = False
    vitoria_maquina = False
    empate = False

    jogador = False
    computador = False

    vitoria_humana = False
    vitoria_maquina = False

    x1 = False
    x2 = False
    x3 = False
    x4 = False
    x5 = False
    x6 = False
    x7 = False
    x8 = False
    x9 = False

    b1 = False
    b2 = False
    b3 = False
    b4 = False
    b5 = False
    b6 = False
    b7 = False
    b8 = False
    b9 = False

    clicavel1 = True
    clicavel2 = True
    clicavel3 = True
    clicavel4 = True
    clicavel5 = True
    clicavel6 = True
    clicavel7 = True
    clicavel8 = True
    clicavel9 = True

    defender = True

    tela.fill((5, 5, 5))
    tela.blit(imagem_fundo, (345, 45))


# Cria os X que aparecem na tela
class X:
    def __init__(self, espaco, x, y):
        global jogador, computador, espaco_clique1, espaco_clique2, espaco_clique3, espaco_clique4, espaco_clique5,\
            espaco_clique6, espaco_clique7, espaco_clique8, espaco_clique9, x1, x2, x3, x4, x5, x6, x7, x8, x9

        x_jogador = pygame.transform.scale(x_imgem, (200, 200))

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if espaco.collidepoint(evento.pos):
                    tela.blit(x_jogador, (x, y))

                    if jogador:
                        if quantidade_x == quantidade_bolas:
                            if espaco == espaco_clique1:
                                x1 = True

                            if espaco == espaco_clique2:
                                x2 = True

                            if espaco == espaco_clique3:
                                x3 = True

                            if espaco == espaco_clique4:
                                x4 = True

                            if espaco == espaco_clique5:
                                x5 = True

                            if espaco == espaco_clique6:
                                x6 = True

                            if espaco == espaco_clique7:
                                x7 = True

                            if espaco == espaco_clique8:
                                x8 = True

                            if espaco == espaco_clique9:
                                x9 = True


# Cria as bolas que aparecem na tela
class Bola:
    def __init__(self,  x, y):
        bola_jogador = pygame.transform.scale(bola_imagem, (200, 200))
        tela.blit(bola_jogador, (x, y))


# Cria as linhas que traçam a vitória
class Linha:
    def __init__(self, x_inicial, y_inicial, x_terminal, y_terminal):
        pygame.draw.line(tela, (255, 255, 255), (x_inicial, y_inicial), (x_terminal, y_terminal), 15)


# Programa que mantem a janela aberta
while janela_aberta:
    pygame.time.delay(30)
    lista_x = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
    lista_b = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    quantidade_x = lista_x.count(True)
    quantidade_bolas = lista_b.count(True)

    # Verifica se é a vez do jogador
    if quantidade_x == quantidade_bolas:
        jogador = True
        computador = False

    # Legendas que aparecem na tela
    fonte_instrucao = pygame.font.Font(None, 35)
    mensagem_de_afronta = "ME VENÇA NO JOGO DA VELHA!!! SE FOR CAPAZ, É CLÁRO HAHAHAHAHAHAHAH"
    mensagem_inicial = fonte_instrucao.render(mensagem_de_afronta, True, (255, 255, 255))
    mensagem_para_reiniciar = "PRESSIONE A LETRA 'R' PARA TENTAR NOVAMENTE"
    aviso_para_reiniciar = fonte_instrucao.render(mensagem_para_reiniciar, True, (255, 255, 255))
    posicoes(aviso_para_reiniciar, 332, 665)
    posicoes(mensagem_inicial, 160, 10)

    fonte_pontos = pygame.font.Font(None, 35)
    pontuacao_x = str(f"JOGADOR = {contador_x}")
    pontuacao_bola = str(f"COMPUTADOR = {contador_bola}")
    pontuacao_empate = str(f"EMPATES = {contador_empate}")
    mensagem_pontuacao_x = fonte_pontos.render(pontuacao_x, True, (255, 255, 255))
    mensagem_pontuacao_bola = fonte_pontos.render(pontuacao_bola, True, (255, 255, 255))
    mensagem_pontuacao_empate = fonte_pontos.render(pontuacao_empate, True, (255, 255, 255))
    posicoes(mensagem_pontuacao_x, 50, 350)
    posicoes(mensagem_pontuacao_bola, 50, 250)
    posicoes(mensagem_pontuacao_empate, 50, 150)

    # Verifica se o jogador pressionou o botão de reiniciar
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                reiniciar()

        # Verifica se o jogador apertou o botão de fechar o jogo
        if evento.type == pygame.QUIT:
            janela_aberta = False

    # Vez do jogador
    if jogador:
        if clicavel1:
            espaco_x1 = X(espaco_clique1, 350, 50)
        if clicavel2:
            espaco_x2 = X(espaco_clique2, 545, 50)
        if clicavel3:
            espaco_x3 = X(espaco_clique3, 738, 50)
        if clicavel4:
            espaco_x4 = X(espaco_clique4, 350, 245)
        if clicavel5:
            espaco_x5 = X(espaco_clique5,  545, 245)
        if clicavel6:
            espaco_x6 = X(espaco_clique6, 738, 245)
        if clicavel7:
            espaco_x7 = X(espaco_clique7, 350, 437)
        if clicavel8:
            espaco_x8 = X(espaco_clique8, 545, 437)
        if clicavel9:
            espacox9 = X(espaco_clique9, 738, 437)
        jogador = False
        computador = True

    # Vez do computador
    if computador:
        if clicavel1:
            if b1:
                bola1 = Bola(350, 50)
                clicavel1 = False
        if clicavel2:
            if b2:
                bola2 = Bola(545, 50)
                clicavel2 = False
        if clicavel3:
            if b3:
                bola3 = Bola(738, 50)
                clicavel3 = False
        if clicavel4:
            if b4:
                bola4 = Bola(350, 245)
                clicavel4 = False
        if clicavel5:
            if b5:
                bola5 = Bola(545, 245)
                clicavel5 = False
        if clicavel6:
            if b6:
                bola6 = Bola(738, 245)
                clicavel6 = False
        if clicavel7:
            if b7:
                bola7 = Bola(350, 437)
                clicavel7 = False
        if clicavel8:
            if b8:
                bola8 = Bola(545, 437)
                clicavel8 = False
        if clicavel9:
            if b9:
                bola9 = Bola(738, 437)
                clicavel9 = False

        # O computador só vai jogar se for a vez dele
        if quantidade_x > quantidade_bolas:
            computador = False

        # Empate
        if quantidade_x == 5 and quantidade_bolas == 4:
            empate = True

        # Todas as possibilidades de jogadas no jogo da velha 3x3
        # x = Pontas, bola = meio
        if x1:
            if x5 is False and b5 is False:
                b5 = True
            b1 = False
            clicavel1 = False

        elif x3:
            if x5 is False and b5 is False:
                b5 = True
            b3 = False
            clicavel3 = False

        elif x7:
            if x5 is False and b5 is False:
                b5 = True
            b7 = False
            clicavel7 = False

        elif x9:
            if x5 is False and b5 is False:
                b5 = True
            b9 = False
            clicavel9 = False

        # Jogador joga no meio
        if x5:
            if x3 is False and b3 is False:
                b3 = True
            b5 = False
            clicavel5 = False

        # Jogador joga no meio 2° parte
        if x5 and x7:
            if x1 is False and b1 is False:
                b1 = True
            b5 = False
            b7 = False
            clicavel5 = False
            clicavel7 = False

        # Jogador joga na lateral 1
        if x2:
            if x5 is False and b5 is False:
                b5 = True
            b2 = False
            clicavel2 = False

        # Jogador joga na lateral 2
        if x4:
            if x5 is False and b5 is False:
                b5 = True
            b4 = False
            clicavel4 = False

        # Jogador joga na lateral 3
        if x6:
            if x5 is False and b5 is False:
                b5 = True
            b6 = False
            clicavel6 = False

        # Jogador joga na lateral 4
        if x8:
            if x5 is False and b5 is False:
                b5 = True
            b8 = False
            clicavel8 = False

        # Jogada lateral, continuação horizontal
        if x4 and x6 and b5:
            if x3 is False and x9 is False and x1 is False and x7 is False and x8 is False and x2 is False\
                    and x5 is False and b3 is False:
                b3 = True
            b4 = False
            b6 = False
            clicavel4 = False
            clicavel6 = False

        # Jogada lateral, continuação vertical
        if x2 and x8 and b5:
            if x7 is False and x3 is False and x9 is False and x1 is False and x4 is False and x5 is False\
                    and x6 is False and b7 is False:
                b7 = True
            b2 = False
            b8 = False
            clicavel2 = False
            clicavel8 = False

        # Jogada lateral, continuação no canto superior direito
        if x4 and x3 and b5:
            if x8 is False and x7 is False and x1 is False and x2 is False and x5 is False and x6 is False\
                    and x9 is False and b8 is False:
                b8 = True
            b4 = False
            b3 = False
            clicavel4 = False
            clicavel3 = False

        # Jogada lateral, continuação no canto inferior direito
        if x4 and x9 and b5:
            if x2 is False and x1 is False and x7 is False and x3 is False and x5 is False and x6 is False\
                    and x8 is False and b2 is False:
                b2 = True
            b4 = False
            b9 = False
            clicavel4 = False
            clicavel9 = False

        # Jogada lateral, continuação no canto superior esquerdo
        if x6 and x1 and b5:
            if x8 is False and x9 is False and x3 is False and x2 is False and x4 is False and x5 is False\
                    and x7 is False and b8 is False:
                b8 = True
            b6 = False
            b1 = False
            clicavel6 = False
            clicavel1 = False

        # Jogada lateral, continuação no canto inferior esquerdo
        if x6 and x7 and b5:
            if x2 is False and x3 is False and x4 is False and x9 is False and x1 is False and x5 is False\
                    and x8 is False and b2 is False:
                b2 = True
            b6 = False
            b7 = False
            clicavel6 = False
            clicavel7 = False

        # Jogada na lateral de baixo, continuação no canto superior esquerdo
        if x8 and x1 and b5:
            if x6 is False and x7 is False and x2 is False and x3 is False and x4 is False and x5 is False\
                    and x9 is False and b6 is False:
                b6 = True
            b8 = False
            b1 = False
            clicavel8 = False
            clicavel1 = False

        # Jogada na lateral de baixo, continuação no canto superior direito
        if x8 and x3 and b5:
            if x4 is False and x9 is False and x2 is False and x1 is False and x5 is False and x6 is False\
                    and x7 is False and b4 is False:
                b4 = True
            b8 = False
            b3 = False
            clicavel8 = False
            clicavel3 = False

        # Jogada na lateral de cima, continuação no canto inferior direito
        if x2 and x9 and b5:
            if x4 is False and x3 is False and x1 is False and x5 is False and x6 is False and x7 is False\
                    and x8 is False and b4 is False:
                b4 = True
            b2 = False
            b9 = False
            clicavel2 = False
            clicavel9 = False

        # Jogada na lateral de cima, continuação no canto inferior esquerdo
        if x2 and x7 and b5:
            if x6 is False and x1 is False and x4 is False and x3 is False and x5 is False and x8 is False\
                    and x9 is False and b6 is False:
                b6 = True
            b2 = False
            b7 = False
            clicavel2 = False
            clicavel7 = False

        # jogador joga no meio da lateral esquerda e no meio da lateral de cima
        if x4 and x2 and b5:
            if x3 is False and x1 is False and x5 is False and x6 is False and x7 is False and x8 is False\
                    and x9 is False and b3 is False:
                b3 = True
            b4 = False
            b2 = False
            clicavel4 = False
            clicavel2 = False

        # jogador joga no meio da lateral direita e no meio da lateral de cima
        if x6 and x2 and b5:
            if x1 is False and x3 is False and x5 is False and x4 is False and x7 is False and x8 is False\
                    and x9 is False and b1 is False:
                b1 = True
            b6 = False
            b2 = False
            clicavel6 = False
            clicavel2 = False

        # jogador joga no meio da lateral esquerda e no meio da lateral de baixo
        if x4 and x8 and b5:
            if x3 is False and x1 is False and x5 is False and x6 is False and x7 is False and x2 is False\
                    and x9 is False and b9 is False:
                b9 = True
            b4 = False
            b8 = False
            clicavel4 = False
            clicavel8 = False

        # jogador joga no meio da lateral direita e no meio da lateral de baixo
        if x6 and x8 and b5:
            if x1 is False and x3 is False and x5 is False and x4 is False and x7 is False and x2 is False\
                    and x9 is False and b7 is False:
                b7 = True
            b6 = False
            b8 = False
            clicavel6 = False
            clicavel8 = False

        # Jogador joga em canto superior direito e em canto inferior esquerdo
        if x3 and x7 and b5:
            if x8 is False and x1 is False and x2 is False and x4 is False and x5 is False and x6 is False\
                    and x9 is False and b2 is False:
                b2 = True
            b3 = False
            b7 = False
            clicavel3 = False
            clicavel7 = False

        # Jogador joga em canto superior esquerdo e em canto inferior direito
        if x1 and x9 and b5:
            if x8 is False and x3 is False and x2 is False and x4 is False and x5 is False and x6 is False\
                    and x7 is False and b8 is False:
                b8 = True
            b1 = False
            b9 = False
            clicavel1 = False
            clicavel9 = False

        # Primeira Possibilidade (inicio)
        # Empate
        if x1 and x7 and x6 and b5 and b4:
            if x2 is False and b2 is False:
                b2 = True
            b6 = False
            b7 = False
            b1 = False
            clicavel1 = False
            clicavel7 = False
            clicavel6 = False

        # Empate Final
        if x1 and x8 and x7 and x6 and b5 and b4 and b2:
            if x9 is False and b9 is False:
                b9 = True
            b8 = False
            b6 = False
            b7 = False
            b1 = False
            clicavel1 = False
            clicavel8 = False
            clicavel7 = False
            clicavel6 = False
        # Primeira Possibilidade (Fim)

        # Segunda Possibilidade (incio)
        # Empate
        if x1 and x3 and x8 and b5 and b2:
            if x6 is False and b6 is False and x7 is False and x4 is False:
                b6 = True
            b1 = False
            b3 = False
            b8 = False
            clicavel1 = False
            clicavel3 = False
            clicavel8 = False

        # Empate Final
        if x1 and x3 and x8 and x4 and b5 and b2 and b6:
            if x7 is False and b7 is False:
                b7 = True
            b1 = False
            b3 = False
            b8 = False
            b4 = False
            clicavel1 = False
            clicavel3 = False
            clicavel8 = False
            clicavel4 = False
        # Segunda Possibilidade (Fim)

        # Terceira Possibilidade (incio)
        # Empate
        if x3 and x9 and x4 and b5 and b6:
            if x8 is False and b8 is False:
                b8 = True
            b3 = False
            b9 = False
            b4 = False
            clicavel3 = False
            clicavel9 = False
            clicavel4 = False

        # Empate Final
        if x3 and x9 and x4 and x2 and b5 and b6 and b8:
            if x1 is False and b1 is False:
                b1 = True
            b3 = False
            b9 = False
            b4 = False
            b2 = False
            clicavel3 = False
            clicavel9 = False
            clicavel4 = False
            clicavel2 = False
        # Terceira Possibilidade (Fim)

        # Quarta Possibilidade (incio)
        # Empate
        if x7 and x9 and x2 and b5 and b8:
            if x4 is False and b4 is False and x6 is False:
                b4 = True
            b7 = False
            b9 = False
            b2 = False
            clicavel7 = False
            clicavel9 = False
            clicavel2 = False

        # Empate Final
        if x7 and x9 and x2 and x6 and b8 and b5 and b4:
            if x3 is False and b3 is False:
                b3 = True
            b7 = False
            b9 = False
            b2 = False
            b6 = False
            clicavel7 = False
            clicavel9 = False
            clicavel2 = False
            clicavel6 = False
        # Quarta Possibilidade (Fim)

        # Empate Final 1
        if x1 and x2 and x6 and x7 and b3 and b4 and b5:
            if x8 is False and b8 is False:
                b8 = True
            b1 = False
            b2 = False
            b6 = False
            b7 = False
            clicavel1 = False
            clicavel2 = False
            clicavel6 = False
            clicavel7 = False

        # Empate Final 2
        if x1 and x3 and x6 and x8 and b2 and b5 and b9:
            if x4 is False and b4 is False and b7 is False:
                b4 = True
            b1 = False
            b3 = False
            b6 = False
            b8 = False
            clicavel1 = False
            clicavel3 = False
            clicavel6 = False
            clicavel8 = False

        # Empate Final 3
        if x3 and x4 and x8 and x9 and b5 and b6 and b7:
            if x2 is False and b2 is False:
                b2 = True
            b3 = False
            b4 = False
            b8 = False
            b9 = False
            clicavel3 = False
            clicavel4 = False
            clicavel8 = False
            clicavel9 = False

        # Empate Final 4
        if x2 and x4 and x7 and x9 and b1 and b5 and b8:
            if x6 is False and b6 is False and b3 is False:
                b6 = True
            b2 = False
            b4 = False
            b7 = False
            b9 = False
            clicavel2 = False
            clicavel4 = False
            clicavel7 = False
            clicavel9 = False

        # Empate Final 5
        if x2 and x5 and x7 and x9 and b1 and b3 and b8:
            if x4 is False and b4 is False:
                b4 = True
            b2 = False
            b5 = False
            b7 = False
            b9 = False
            clicavel2 = False
            clicavel5 = False
            clicavel7 = False
            clicavel9 = False

        # Empate Final 6
        if x2 and x6 and x7 and x9 and b3 and b5 and b8:
            if x4 is False and b4 is False and x1 is False and b1 is False:
                b4 = True
            b2 = False
            b6 = False
            b7 = False
            b9 = False
            clicavel2 = False
            clicavel6 = False
            clicavel7 = False
            clicavel9 = False

        # Empate Final 7
        if x1 and x3 and x4 and x8 and b2 and b5 and b7:
            if x9 is False and b9 is False and x6 is False and b6 is False:
                b9 = True
            b1 = False
            b3 = False
            b4 = False
            b8 = False
            clicavel1 = False
            clicavel3 = False
            clicavel4 = False
            clicavel8 = False

        # Empate Final 8
        if x1 and x5 and x6 and x7 and b3 and b4 and b9:
            if x2 is False and b2 is False and x8 is False and b8 is False:
                b2 = True
            b1 = False
            b5 = False
            b6 = False
            b7 = False
            clicavel1 = False
            clicavel5 = False
            clicavel6 = False
            clicavel7 = False

        # Esse código só vai acontecer se for a vez do computador
        if quantidade_x > quantidade_bolas:

            # POSSIBILIDADES DE GANHO DO COMPUTADOR
            # Computador ganha na primeira faixa
            if b1 and b2 and b3 is False and x3 is False:
                b3 = True
                linha1 = Linha(375, 150, 920, 150)
                vitoria_maquina = True
                defender = False
            elif b2 and b3 and b1 is False and x1 is False:
                b1 = True
                linha1 = Linha(375, 150, 920, 150)
                vitoria_maquina = True
                defender = False
            elif b1 and b3 and b2 is False and x2 is False:
                b2 = True
                linha1 = Linha(375, 150, 920, 150)
                vitoria_maquina = True
                defender = False

            # Computador ganha na segunda faixa
            elif b4 and b5 and b6 is False and x6 is False:
                b6 = True
                linha2 = Linha(375, 340, 920, 340)
                vitoria_maquina = True
                defender = False
            elif b5 and b6 and b4 is False and x4 is False:
                b4 = True
                linha2 = Linha(375, 340, 920, 340)
                vitoria_maquina = True
                defender = False
            elif b4 and b6 and b5 is False and x5 is False:
                b5 = True
                linha2 = Linha(375, 340, 920, 340)
                vitoria_maquina = True
                defender = False

            # Computador ganha na terceira faixa
            elif b7 and b8 and b9 is False and x9 is False:
                b9 = True
                linha3 = Linha(375, 535, 920, 535)
                vitoria_maquina = True
                defender = False
            elif b8 and b9 and b7 is False and x7 is False:
                b7 = True
                linha3 = Linha(375, 535, 920, 535)
                vitoria_maquina = True
                defender = False
            elif b7 and b9 and b8 is False and x8 is False:
                b8 = True
                linha3 = Linha(375, 535, 920, 535)
                vitoria_maquina = True
                defender = False

            # Computador ganha na primeira coluna
            elif b1 and b4 and b7 is False and x7 is False:
                b7 = True
                coluna1 = Linha(450, 75, 450, 620)
                vitoria_maquina = True
                defender = False
            elif b4 and b7 and b1 is False and x1 is False:
                b1 = True
                coluna1 = Linha(450, 75, 450, 620)
                vitoria_maquina = True
                defender = False
            elif b1 and b7 and b4 is False and x4 is False:
                b4 = True
                coluna1 = Linha(450, 75, 450, 620)
                vitoria_maquina = True
                defender = False

            # Computador ganha na segunda coluna
            elif b2 and b5 and b8 is False and x8 is False:
                b8 = True
                coluna2 = Linha(645, 75, 645, 620)
                vitoria_maquina = True
                defender = False
            elif b5 and b8 and b2 is False and x2 is False:
                b2 = True
                coluna2 = Linha(645, 75, 645, 620)
                vitoria_maquina = True
                defender = False
            elif b2 and b8 and b5 is False and x5 is False:
                b5 = True
                coluna2 = Linha(645, 75, 645, 620)
                vitoria_maquina = True
                defender = False

            # Computador ganha na terceira coluna
            elif b3 and b6 and b9 is False and x9 is False:
                b9 = True
                coluna3 = Linha(840, 75, 840, 620)
                vitoria_maquina = True
                defender = False
            elif b6 and b9 and b3 is False and x3 is False:
                b3 = True
                coluna3 = Linha(840, 75, 840, 620)
                vitoria_maquina = True
                defender = False
            elif b3 and b9 and b6 is False and x6 is False:
                b6 = True
                coluna3 = Linha(840, 75, 840, 620)
                vitoria_maquina = True
                defender = False

            # Computador ganha na diagonal principal
            elif b1 and b5 and b9 is False and x9 is False:
                b9 = True
                diagonalPrincipal = Linha(400, 90, 900, 600)
                vitoria_maquina = True
                defender = False
            elif b5 and b9 and b1 is False and x1 is False:
                b1 = True
                diagonalPrincipal = Linha(400, 90, 900, 600)
                vitoria_maquina = True
                defender = False
            elif b1 and b9 and b5 is False and x5 is False:
                b5 = True
                diagonalPrincipal = Linha(400, 90, 900, 600)
                vitoria_maquina = True
                defender = False

            # Computador ganha na diagonal secundária
            elif b3 and b5 and b7 is False and x7 is False:
                b7 = True
                diagonalSecundaria = Linha(900, 90, 400, 600)
                vitoria_maquina = True
                defender = False
            elif b5 and b7 and b3 is False and x3 is False:
                b3 = True
                diagonalSecundaria = Linha(900, 90, 400, 600)
                vitoria_maquina = True
                defender = False
            elif b3 and b7 and b5 is False and x5 is False:
                b5 = True
                diagonalSecundaria = Linha(900, 90, 400, 600)
                vitoria_maquina = True
                defender = False

            if defender:

                # COMPUTADOR TENTANDO NÃO PERDER
                # Computador evita perder na primeira linha
                if x1 and x2 and x3 is False and b3 is False:
                    b3 = True
                if x2 and x3 and x1 is False and b1 is False:
                    b1 = True
                if x1 and x3 and x2 is False and b2 is False:
                    b2 = True

                # Computador evita perder na segunda linha
                if x4 and x5 and x6 is False and b6 is False:
                    b6 = True
                if x5 and x6 and x4 is False and b4 is False:
                    b4 = True
                if x4 and x6 and x5 is False and b5 is False:
                    b5 = True

                # Computador evita perder na terceira linha
                if x7 and x8 and x9 is False and b9 is False:
                    b9 = True
                if x8 and x9 and x7 is False and b7 is False:
                    b7 = True
                if x7 and x9 and x8 is False and b8 is False:
                    b8 = True

                # Computador evita perder na primeira coluna
                if x1 and x4 and x7 is False and b7 is False:
                    b7 = True
                if x4 and x7 and x1 is False and b1 is False:
                    b1 = True
                if x1 and x7 and x4 is False and b4 is False:
                    b4 = True

                # Computador evita perder na segunda coluna
                if x2 and x5 and x8 is False and b8 is False:
                    b8 = True
                if x5 and x8 and x2 is False and b2 is False:
                    b2 = True
                if x2 and x8 and x5 is False and b5 is False:
                    b8 = True

                # Computador evita perder na terceira coluna
                if x3 and x6 and x9 is False and b9 is False:
                    b9 = True
                if x6 and x9 and x3 is False and b3 is False:
                    b3 = True
                if x3 and x9 and x6 is False and b6 is False:
                    b6 = True

                # Computador evita perder na diagonal principal
                if x1 and x5 and x9 is False and b9 is False:
                    b9 = True
                if x5 and x9 and x1 is False and b1 is False:
                    b1 = True
                if x1 and x9 and x5 is False and b5 is False:
                    b5 = True

                # Computadopr evita perder na diagonal secundária
                if x3 and x5 and x7 is False and b7 is False:
                    b7 = True
                if x5 and x7 and x3 is False and b3 is False:
                    b3 = True
                if x3 and x7 and x5 is False and b5 is False:
                    b5 = True

    # Atualiza o jogo
    pygame.display.update()

# Finaliza o jogo
pygame.quit()
