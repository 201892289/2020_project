import pygame
import random
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(r'enemy.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width  # -20
        self.rect.y = self.rect.height  # -20

        self.direction = random.choice([1, -1])

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 由于x可以精确到小数，故先更新x，再用x更新rect
        self.x += (self.ai_settings.alien_speed_factor *
                   self.direction)  # *random.choice([1,-1])#####
        self.rect.x = self.x
