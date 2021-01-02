import pygame, sys
import test
import input_box
import button
import read_config
import draw_text
import leaderboard

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)
BLACK,WHITE,GRAY = read_config.read_config()


def main_menu():
    click = False

    while True:
        screen.fill(WHITE)
        draw_text.draw_text('main menu', font, BLACK, screen, 20, 20)

        button_1=button.Button(50, 100, 200, 50, text='Start game')
        button_2 = button.Button(50, 200, 200, 50,text='AI game')
        button_3 = button.Button(50, 300, 200, 50, text='Leaderboard')
        button_4 = button.Button(50, 400, 200, 50, text='End game')
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
                game_by_player
            if button_2.click:
                game_by_AI()
            if button_3.click:
                leaderboard.r_w_leaderboard(screen,font,rw="r")
            if button_4.click:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(25)


def options():
    running = True
    input_name_box=input_box.InputBox(100,100,140,32)

    while running:
        screen.fill((0, 0, 0))

        draw_text.draw_text('options', font, (0, 0, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            input_name_box.handle_event(event)

        input_name_box.update()
        input_name_box.draw(screen)


        pygame.display.update()
        mainClock.tick(60)
    return input_name_box.text

def game_by_AI():
    is_AI=True
    name="AI"
    test.game_start(name,is_AI)

def game_by_player():
    running = True
    input_name_box=input_box.InputBox(100,100,140,32)
    name = "Anonymous"
    while running:
        screen.fill((255, 255, 255))
        draw_text.draw_text('Game by player', font, (0, 0, 0), screen, 20, 20)

        button_start_game=button.Button(50, 300, 200, 50, text='Start !')
        button_start_game.draw(screen)

        input_name_box.update()
        input_name_box.draw(screen)

        name=input_name_box.text

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            input_name_box.handle_event(event)
            button_start_game.handle_event(event)

            if button_start_game.click:
                test.game_start(name,None)

        pygame.display.update()
        mainClock.tick(60)
    return input_name_box.text

main_menu()