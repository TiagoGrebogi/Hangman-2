import pygame as pg

# Inicializa o Pygame
pg.init()

# Configurações da tela
width, height = 640, 480
icon = pg.image.load('./thumbnail.png')
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Hangman: The Gathering')
pg.display.set_icon(icon)

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definindo as dimensões e a posição do botão
button_width = 200
button_height = 50
button_x = (width - button_width) // 2
button_y = (height - button_height) // 2

# Função para desenhar o botão
def draw_button(screen, color, x, y, width, height, text):
    pg.draw.rect(screen, color, (x, y, width, height))
    font = pg.font.Font(None, 36)
    text_render = font.render(text, True, BLACK)
    text_rect = text_render.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_render, text_rect)

# Loop principal do jogo
gameRunning = True
while gameRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameRunning = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (button_x <= mouse_x <= button_x + button_width and
                button_y <= mouse_y <= button_y + button_height):
                print("Botão clicado!")

    # Preenchendo a tela com branco
    screen.fill(WHITE)

    # Desenhando o botão
    draw_button(screen, RED, button_x, button_y, button_width, button_height, 'Clique Aqui')

    # Atualizando a tela
    pg.display.flip()

# Encerrando o Pygame
pg.quit()
