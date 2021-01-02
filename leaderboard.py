import pygame,sys
import draw_text
pygame.init()
mainClock = pygame.time.Clock()

def r_w_leaderboard(screen,font,rw=None,name=None,score=None):
    running = True
    write_flag=0
    while running:
        screen.fill((255,255,255))
        draw_text.draw_text('Leaderboard', font, (0, 0, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running =False

        # read from leaderboard.txt and blit on the screen
        if rw == "r":
            f = open("leaderboard.txt")
            lines = f.readlines()
            y_position = 40
            for line in lines:
                draw_text.draw_text(line, font, (0, 0, 0), screen, 20, y_position)
                y_position = y_position + 20
            f.close()
        # write into  leaderboard.txt
        elif rw == "w" and write_flag==0:
            f = open("leaderboard.txt", 'a')
            f.write(str(name) + "      score:" + str(score)+'\n')
            write_flag=1
            f.close()
            return 1

        pygame.display.update()
        mainClock.tick(25)
