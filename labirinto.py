import random
import tkinter as tk

# Gera um labirinto usando o algoritmo de divisão recursiva
def gera_labirinto(largura, altura):
    labirinto = [['#' for _ in range(largura)] for _ in range(altura)]
    
    def divide(x, y, w, h):
        if w <= 1 or h <= 1:
            return

        horizontal = random.choice([True, False])
        if w > h:
            horizontal = False
        elif h > w:
            horizontal = True

        if horizontal:
            if h - 2 < 1:
                return
            wy = y + random.randint(1, h - 2)
            px = x + random.randint(0, w - 1)
            for i in range(w):
                if i != px:
                    labirinto[wy][x + i] = '#'
            divide(x, y, w, wy - y)
            divide(x, wy + 1, w, y + h - wy - 1)
        else:
            if w - 2 < 1:
                return
            wx = x + random.randint(1, w - 2)
            py = y + random.randint(0, h - 1)
            for i in range(h):
                if i != py:
                    labirinto[y + i][wx] = '#'
            divide(x, y, wx - x, h)
            divide(wx + 1, y, x + w - wx - 1, h)

    divide(0, 0, largura, altura)
    labirinto[0][0] = 'S'
    labirinto[altura - 1][largura - 1] = 'E'
    return labirinto

# Função para desenhar o labirinto na interface gráfica
def desenha_labirinto(labirinto):
    for y, linha in enumerate(labirinto):
        for x, bloco in enumerate(linha):
            cor = "black" if bloco == "#" else "white"
            canvas.create_rectangle(x * tamanho, y * tamanho, (x + 1) * tamanho, (y + 1) * tamanho, fill=cor)

# Movimenta o jogador pelo labirinto
def move_jogador(event):
    global jogador_x, jogador_y
    direcoes = {'Up': (0, -1), 'Down': (0, 1), 'Left': (-1, 0), 'Right': (1, 0)}
    if event.keysym in direcoes:
        dx, dy = direcoes[event.keysym]
        novo_x, novo_y = jogador_x + dx, jogador_y + dy
        if 0 <= novo_x < largura and 0 <= novo_y < altura and labirinto[novo_y][novo_x] != '#':
            jogador_x, jogador_y = novo_x, novo_y
            desenha_labirinto(labirinto)
            canvas.create_rectangle(jogador_x * tamanho, jogador_y * tamanho, (jogador_x + 1) * tamanho, (jogador_y + 1) * tamanho, fill="blue")
            if labirinto[jogador_y][jogador_x] == 'E':
                canvas.create_text(largura * tamanho / 2, altura * tamanho / 2, text="Você venceu!", font=("Arial", 24), fill="green")

# Configurações iniciais
largura, altura = 20, 20
tamanho = 20
labirinto = gera_labirinto(largura, altura)
jogador_x, jogador_y = 0, 0

# Interface gráfica
root = tk.Tk()
root.title("Labirinto")
canvas = tk.Canvas(root, width=largura * tamanho, height=altura * tamanho)
canvas.pack()
root.bind("<Key>", move_jogador)
desenha_labirinto(labirinto)
canvas.create_rectangle(jogador_x * tamanho, jogador_y * tamanho, (jogador_x + 1) * tamanho, (jogador_y + 1) * tamanho, fill="blue")
root.mainloop()
