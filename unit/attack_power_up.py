import pygame

from unit.power_up import PowerUp

class AttackPowerUp(PowerUp):
    reward_points = 2
    sprite = pygame.image.load("assets/Damage_PUP.png")

    def __init__(self, *args, **kwargs):
        # load the image for the base class.
        self._base_image = AttackPowerUp.sprite

        super().__init__(*args, **kwargs)
