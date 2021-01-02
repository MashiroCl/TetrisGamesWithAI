import read_config
import pygame

BLACK,WHITE,GRAY=read_config.read_config()

COLOR_INACTIVE = WHITE
COLOR_ACTIVE= GRAY
FONT=pygame.font.Font(None,32)


class Button:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.txt_surface = FONT.render(text, True, BLACK)
        self.click=False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the button
            if self.rect.collidepoint(event.pos):
                self.click=True
            else:
                self.click=False

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, BLACK, self.rect, 2)
