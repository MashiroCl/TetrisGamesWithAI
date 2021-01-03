import read_config
import pygame

BLACK,WHITE,GRAY=read_config.read_config()

COLOR_INACTIVE = WHITE
COLOR_ACTIVE= GRAY
FONT=pygame.font.Font(None,32)


class Button:
    def __init__(self, x, y, w, h, text_x, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.txt_surface = FONT.render(text, True, BLACK)
        self.click=False
        self.text_x=text_x

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the button
            if self.rect.collidepoint(event.pos):
                self.click=True
            else:
                self.click=False

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+self.text_x, self.rect.y+15))
        # Blit the rect.
        pygame.draw.rect(screen, BLACK, self.rect, 2)
