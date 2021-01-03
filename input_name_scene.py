import pygame
import input_box
import draw_text
import button
import sys
import game_scene

def input_name_scene(screen,font,font_text,mainClock):
    running = True
    input_name_box = input_box.InputBox(150, 100, 140, 32)
    name = "Anonymous"
    while running:
        screen.fill((255, 255, 255))
        draw_text.draw_text('Game by player', font, (0, 0, 0), screen, 120, 20)
        draw_text.draw_text('Please enter your name', font_text, (0, 0, 0), screen, 140, 80)
        button_start_game = button.Button(150, 300, 200, 50, 70, text='Start !')
        button_start_game.draw(screen)

        input_name_box.update()
        input_name_box.draw(screen)

        name = input_name_box.text

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            input_name_box.handle_event(event)
            button_start_game.handle_event(event)

            if button_start_game.click:
                game_scene.game_start(name, False)

        pygame.display.update()
        mainClock.tick(60)
    return input_name_box.text