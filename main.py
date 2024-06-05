import pygame as pg
import random

pg.init()

screen_info = pg.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)
pg.display.set_caption('Hangman: The Gathering')

image_path = './background.png'
image = pg.image.load(image_path)
image = pg.transform.scale(image, (screen_width, screen_height))
pg.display.set_icon(image)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def draw_button(screen, color, x, y, width, height, text, text_color):
    button_surface = pg.Surface((width, height), pg.SRCALPHA)
    button_surface.fill((255, 255, 255, 0))
    pg.draw.rect(button_surface, color, (0, 0, width, height), border_radius=12)
    font = pg.font.Font(None, 36)
    text_render = font.render(text, True, text_color)
    text_rect = text_render.get_rect(center=(width // 2, height // 2))
    button_surface.blit(text_render, text_rect)
    screen.blit(button_surface, (x, y))

def draw_letter_card(screen, letter, x, y, width, height, color, text_color):
    pg.draw.rect(screen, color, (x, y, width, height), border_radius=12)
    font = pg.font.Font(None, 48)
    text_render = font.render(letter, True, text_color)
    text_rect = text_render.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_render, text_rect)

def draw_hangman(screen, tries):
    base_x = screen_width // 2 - 100
    base_y = screen_height // 4

    pg.draw.line(screen, BLACK, (base_x, base_y + 200), (base_x + 200, base_y + 200), 5)
    pg.draw.line(screen, BLACK, (base_x + 100, base_y + 200), (base_x + 100, base_y), 5)
    pg.draw.line(screen, BLACK, (base_x + 100, base_y), (base_x + 150, base_y), 5)
    pg.draw.line(screen, BLACK, (base_x + 150, base_y), (base_x + 150, base_y + 50), 5)
    if tries >= 1:
        pg.draw.circle(screen, BLACK, (base_x + 150, base_y + 70), 20, 5)
    if tries >= 2:
        pg.draw.line(screen, BLACK, (base_x + 150, base_y + 90), (base_x + 150, base_y + 140), 5)
    if tries >= 3:
        pg.draw.line(screen, BLACK, (base_x + 150, base_y + 100), (base_x + 120, base_y + 120), 5)
    if tries >= 4:
        pg.draw.line(screen, BLACK, (base_x + 150, base_y + 100), (base_x + 180, base_y + 120), 5)
    if tries >= 5:
        pg.draw.line(screen, BLACK, (base_x + 150, base_y + 140), (base_x + 120, base_y + 170), 5)
    if tries >= 6 :
        pg.draw.line(screen, BLACK, (base_x + 150, base_y + 140), (base_x + 180, base_y + 170), 5)

words = ['PYTHON', 'JAVA', 'JAVASCRIPT', 'CPLUSPLUS', 'RUBY', 'SWIFT', 'KOTLIN', 'GO', 'RUST', 'TYPESCRIPT']

word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 0
max_attempts = 6

button_width = 200
button_height = 50
buttons = [
    {'color': BLACK, 'x': (screen_width - button_width) // 2, 'y': (screen_height - 150) // 2, 'width': button_width, 'height': button_height, 'text': 'JOGAR', 'text_color': WHITE},
    {'color': BLACK, 'x': (screen_width - button_width) // 2, 'y': (screen_height - 30) // 2, 'width': button_width, 'height': button_height, 'text': 'SAIR', 'text_color': WHITE}
]

show_buttons = True

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_buttons = []
for i, letter in enumerate(letters):
    row = i // 9
    col = i % 9
    x = 50 + col * 70
    y = screen_height - 220 + row * 70
    letter_buttons.append({'letter': letter, 'x': x, 'y': y, 'width': 60, 'height': 60, 'color': WHITE, 'text_color': BLACK})

gameRunning = True
while gameRunning:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameRunning = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if show_buttons:
                for button in buttons:
                    if (button['x'] <= mouse_x <= button['x'] + button['width'] and
                        button['y'] <= mouse_y <= button['y'] + button['height']):
                        print(f"{button['text']} foi clicado")
                        if button['text'] == 'JOGAR':
                            show_buttons = False  # Esconder os botões
                        elif button['text'] == 'SAIR':
                            gameRunning = False
            else:
                for letter_button in letter_buttons:
                    if (letter_button['x'] <= mouse_x <= letter_button['x'] + letter_button['width'] and
                        letter_button['y'] <= mouse_y <= letter_button['y'] + letter_button['height']):
                        selected_letter = letter_button['letter']
                        print(f"Letra {selected_letter} foi clicada")
                        if selected_letter in word:
                            for i, letter in enumerate(word):
                                if letter == selected_letter:
                                    guessed[i] = selected_letter
                        else:
                            attempts += 1
                        letter_buttons.remove(letter_button)
                        break

    screen.blit(image, (0, 0))

    if show_buttons:
        for button in buttons:
            draw_button(screen, button['color'], button['x'], button['y'], button['width'], button['height'], button['text'], button['text_color'])
    else:
        draw_hangman(screen, attempts)
        
        # Desenhando a palavra a ser adivinhada
        font = pg.font.Font(None, 72)
        guessed_word = font.render(' '.join(guessed), True, BLACK)
        screen.blit(guessed_word, (screen_width // 2 - guessed_word.get_width() // 2, screen_height // 4 + 250))
        
        # Desenhando as letras em formato de cartas
        for letter_button in letter_buttons:
            draw_letter_card(screen, letter_button['letter'], letter_button['x'], letter_button['y'], letter_button['width'], letter_button['height'], letter_button['color'], letter_button['text_color'])
        
        # Verificar se o jogo terminou
        if '_' not in guessed:
            game_over_text = "Você ganhou!"
            gameRunning = False
        elif attempts >= max_attempts:
            game_over_text = f"Você perdeu! A palavra era: {word}"
            gameRunning = False

    # Atualizando a tela
    pg.display.flip()

    # Se o jogo terminou, mostrar mensagem
    if not gameRunning and not show_buttons:
        screen.fill(WHITE)
        font = pg.font.Font(None, 72)
        game_over_render = font.render(game_over_text, True, BLACK)
        screen.blit(game_over_render, (screen_width // 2 - game_over_render.get_width() // 2, screen_height // 2 - game_over_render.get_height() // 2))
        pg.display.flip()
        pg.time.wait(3000)
        break

# Encerrando o Pygame
pg.quit()
