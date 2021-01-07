import pygame,sys
import draw_text
pygame.init()
mainClock = pygame.time.Clock()

def r_w_leaderboard(screen,font,font_text,rw=None,name=None,score=None):
    running = True
    write_flag=0
    while running:

        # read from leaderboard.txt and blit on the screen
        if rw == "r":
            screen.fill((255, 255, 255))
            draw_text.draw_text('Leaderboard', font, (0, 0, 0), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            f = open("leaderboard.txt")
            lines = f.readlines()
            y_position = 50
            for line in lines:
                draw_text.draw_text(line[:-1], font_text, (0, 0, 0), screen, 20, y_position)
                y_position = y_position + 25
            f.close()
        # write into  leaderboard.txt
        elif rw == "w" and write_flag==0:
            f = open("leaderboard.txt", 'a')
            f.write(str(name) + "      score:" + str(score)+'\n')
            f.close()
            return 1

        pygame.display.update()
        mainClock.tick(25)
