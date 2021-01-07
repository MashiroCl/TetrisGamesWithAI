import pygame
import AI_player
import leaderboard
from Figure_and_Tetris import Tetris,colors

def game_start(name,is_AI):
    # Initialize the game engine
    pygame.init()

    # Define colors for figure
    BLACK=(0,0,0)
    WHITE=(255,255,255)
    GRAY=(128,128,128)

    size=(400,500)
    screen=pygame.display.set_mode(size)

    pygame.display.set_caption("Tetris Games With AI")

    # Loop till the player clicks the close button
    done=False
    time_clock=pygame.time.Clock()
    fps=25
    #screen size 20*10 blocks
    game=Tetris(20,10)
    counter=0

    pressing_down=False

    while not done:
        if game.figure is None:
            game.new_figure()
        counter+=1
        if counter>9999999:
            counter=0

        if counter%(fps//game.level//2)==0 or pressing_down:
            if game.state=="start":
                game.go_down()

        # for event in pygame.event.get():
        if is_AI ==True:
            AI_action = AI_player.run_ai(game.field, game.figure, game.width, game.height)
        elif is_AI==False:
            AI_action = []


        for event in list(pygame.event.get())+AI_action:
            if event.type==pygame.QUIT:
                done=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    game.rotate()
                if event.key==pygame.K_DOWN:
                    pressing_down=True
                if event.key==pygame.K_LEFT:
                    game.go_side(-1)
                if event.key==pygame.K_RIGHT:
                    game.go_side(1)
                if event.key==pygame.K_SPACE:
                    game.go_space()
                if event.key==pygame.K_ESCAPE:
                    game.__init__(20,10)

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                pressing_down=False

        screen.fill(WHITE)

        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen,GRAY,[game.x+game.zoom*j,game.y+game.zoom*i,
                                              game.zoom,game.zoom],1)
                if game.field[i][j]>0:
                    pygame.draw.rect(screen,colors[game.field[i][j]],
                                     [game.x+game.zoom*j+1,game.y+game.zoom*i+1,
                                      game.zoom-2,game.zoom-1])

        if game.figure is not None:
            for i in range(4):
                for j in range(4):
                    p=i*4+j
                    if p in game.figure.image():
                        pygame.draw.rect(screen,colors[game.figure.color],
                                         [game.x+game.zoom*(j+game.figure.x)+1,
                                          game.y+game.zoom*(i+game.figure.y)+1,
                                          game.zoom-2,game.zoom-2])

        font = pygame.font.SysFont('Calibri',25,True,False)
        font1=pygame.font.SysFont('Calibri',65,True,False)
        text_score=font.render("Score: "+str(game.score),True,BLACK)
        text_name = font.render("Name: " + str(name), True, BLACK)
        text_game_over=font1.render("Game Over",True,(245,125,0))
        text_game_over1=font1.render("Press ESC",True,(255,215,0))

        screen.blit(text_score, [0,0])
        screen.blit(text_name, [0,20])
        if game.state=="gameover":
            screen.blit(text_game_over,[20,200])
            screen.blit(text_game_over1,[25,265])

        pygame.display.flip()
        time_clock.tick(fps)

    print(name,game.score)
    leaderboard.r_w_leaderboard(screen,font,font_text=None,rw="w",name=name,score=game.score)
    return name,game.score
