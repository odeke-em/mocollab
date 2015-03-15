import pygame

from unit.power_up import PowerUp

class SpeedPowerUp(PowerUp):
    reward_points = 2
    sprite = pygame.image.load("assets/Speed_PUP.png")

    def __init__(self, *args, **kwargs):
        # load the image for the base class.
        self._base_image = SpeedPowerUp.sprite

        super().__init__(*args, **kwargs)
