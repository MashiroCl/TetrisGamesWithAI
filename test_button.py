from unittest import TestCase
from button import Button
import pygame
pygame.init()


class TestButton(TestCase):
    def test_init(self):
        self.button=Button(100, 100, 200, 50,40, text='Test')

    def test_handle_event(self):
        self.button = Button(100, 100, 200, 50, 40, text='Test')
        for event in pygame.event.get():
            self.button.handle_event(event)

    def test_draw(self):
        self.button = Button(100, 100, 200, 50, 40, text='Tes›t')
        screen = pygame.display.set_mode((400, 500), 0, 32)
        self.button.draw(screen)

