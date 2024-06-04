import pygame as pg

pg.init()

# Configurações da tela para preencher 100% da tela
screen_info = pg.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)
pg.display.set_caption('Hangman: The Gathering')

# Carrega e redimensiona a imagem para preencher a tela
image_path = './background.png'
image = pg.image.load(image_path)
image = pg.transform.scale(image, (screen_width, screen_height))
pg.display.set_icon(image)

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Função para desenhar o botão com fundo transparente
def draw_button(screen, color, x, y, width, height, text, text_color):
    button_surface = pg.Surface((width, height), pg.SRCALPHA)  # Criando uma superfície com suporte a transparência
    button_surface.fill((255, 255, 255, 0))  # Preenchendo a superfície com transparência total
    pg.draw.rect(button_surface, color, (0, 0, width, height), border_radius=12)  # Desenhando o retângulo com bordas arredondadas
    font = pg.font.Font(None, 36)
    text_render = font.render(text, True, text_color)  # Renderizando o texto com a cor especificada
    text_rect = text_render.get_rect(center=(width // 2, height // 2))
    button_surface.blit(text_render, text_rect)
    screen.blit(button_surface, (x, y))

# Coordenadas e tamanhos dos botões
button_width = 200
button_height = 50
buttons = [
    {'color': BLACK, 'x': (screen_width - button_width) // 2, 'y': (screen_height - 150) // 2, 'width': button_width, 'height': button_height, 'text': 'JOGAR', 'text_color': WHITE},
    {'color': BLACK, 'x': (screen_width - button_width) // 2, 'y': (screen_height - 30) // 2, 'width': button_width, 'height': button_height, 'text': 'OPÇÕES', 'text_color': WHITE},
    {'color': BLACK, 'x': (screen_width - button_width) // 2, 'y': (screen_height + 90) // 2, 'width': button_width, 'height': button_height, 'text': 'SAIR', 'text_color': WHITE}
]

# Loop principal do jogo
gameRunning = True
while gameRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameRunning = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for button in buttons:
                if (button['x'] <= mouse_x <= button['x'] + button['width'] and
                    button['y'] <= mouse_y <= button['y'] + button['height']):
                    print(f"{button['text']} foi clicado")
                    if button['text'] == 'SAIR':
                        gameRunning = False

    # Preenchendo a tela com a imagem redimensionada
    screen.blit(image, (0, 0))

    # Desenhando os botões
    for button in buttons:
        draw_button(screen, button['color'], button['x'], button['y'], button['width'], button['height'], button['text'], button['text_color'])

    # Atualizando a tela
    pg.display.flip()

# Encerrando o Pygame
pg.quit()
