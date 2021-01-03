import pygame, sys
import game_scene
import button
import read_config
import draw_text
import leaderboard
import input_name_scene

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

#Title font
font = pygame.font.SysFont(None, 45)
#Text font
font_text = pygame.font.SysFont(None, 30)

BLACK,WHITE,GRAY = read_config.read_config()


def main_menu():
    click = False

    while True:
        screen.fill(WHITE)
        draw_text.draw_text('Tetris game with AI', font, BLACK, screen, 120, 20)

        button_1=button.Button(150, 100, 200, 50,40, text='Start game')
        button_2 = button.Button(150, 200, 200, 50,60,text='AI game')
        button_3 = button.Button(150, 300, 200, 50,35, text='Leaderboard')
        button_4 = button.Button(150, 400, 200, 50,50, text='End game')
        button_boxes=[button_1,button_2,button_3,button_4]

        for each in button_boxes:
            each.draw(screen)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            for each in button_boxes:
                each.handle_event(event)

            if button_1.click:
                game_by_player()
            if button_2.click:
                game_by_AI()
            if button_3.click:
                show_leaderboard(screen,font,font_text)
            if button_4.click:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(25)


def game_by_AI():
    is_AI=True
    name="AI"
    game_scene.game_start(name, is_AI)

def game_by_player():
    input_name=input_name_scene.input_name_scene(screen,font,font_text,mainClock)
    return input_name

def show_leaderboard(screen,font_title,font_text):
    leaderboard.r_w_leaderboard(screen, font_title,font_text, rw="r")

main_menu()