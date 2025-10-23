import os

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        print("Initializing Ship...")

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "images", "ship.bmp")

        print("Looking for image at:", image_path)
        print("File exists:", os.path.exists(image_path))

        # Stat each new ship at bottom center of the screen.
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value fo the ships's horizontal position.
        self.x = float(self.rect.x)

        print("Ship image loaded successfully.")
        #  Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ship's postition based on the movement flag.
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
