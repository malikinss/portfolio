import pygame
import sys


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def calculate_coordinate(obj_1_size, obj_2_size):
    return (obj_1_size - obj_2_size) / 2


def get_coordinate(axis, screen, text):
    if axis == 'x':
        return calculate_coordinate(screen.get_width(), text.get_width())
    elif axis == 'y':
        return calculate_coordinate(screen.get_height(), text.get_height())
    else:
        print(f"Axis {axis} doesn't exist")


def draw_text(text_to_display, color, surface):
    text_obj = font.render(text_to_display, True, color)

    text_x_pos = get_coordinate('x', surface, text_obj)
    text_y_pos = get_coordinate('y', surface, text_obj)

    text_coordinates = (text_x_pos, text_y_pos)

    surface.blit(text_obj, text_coordinates)

    return text_obj


def draw_frame_for_text(surface, color, text, contur_width):
    rect_x_pos = get_coordinate('x', surface, text) - 10
    rect_y_pos = get_coordinate('y', surface, text) - 10

    rect_height = text.get_height() + 20
    rect_weight = text.get_width() + 20

    rect_settings = (rect_x_pos, rect_y_pos, rect_weight, rect_height)

    pygame.draw.rect(surface, color, rect_settings, contur_width)


def get_mouse_pos_if_clicked():
    mouse_pos = None
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

    return mouse_pos


# initialize game
pygame.init()

# initialize sound mixer
pygame.mixer.init()
pygame.mixer.music.load("any_project/resources/shortbeep.mp3")

# define screen
screen = pygame.display.set_mode((320, 240))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
text_colors = [BLACK, RED]

BLINK = 500
mouse_pos = None

# define font object
font = pygame.font.Font(None, 26)

time = pygame.time

count = 0

one_second_mark_reached = False
last_time = 0

while True:
    if one_second_mark_reached:
        count += 1

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

    text_to_display = "Hello World, My name is Sam!"
    current_color = text_colors[count % 2]
    text = draw_text(text_to_display, current_color, screen)

    draw_frame_for_text(screen, BLACK, text, 1)

    img_source = pygame.image.load("any_project/resources/star.png")

    if mouse_pos is not None:
        img_x_pos = mouse_pos[0] - 16
        img_y_pos = mouse_pos[1] - 16
    else:
        img_x_pos = (screen.get_width() / 2) - 16
        img_y_pos = get_coordinate("y", screen, text) - 60

    img_position = (img_x_pos, img_y_pos)
    screen.blit(img_source, img_position)

    if one_second_mark_reached:
        pygame.mixer.music.play()

    pygame.display.flip()

    one_second_mark_reached = False

    cur_time = time.get_ticks()

    if cur_time - last_time > 1000:
        last_time = cur_time
        one_second_mark_reached = True
