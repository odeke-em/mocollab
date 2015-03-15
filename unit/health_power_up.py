import pygame

from unit.power_up import PowerUp

class HealthPowerUp(PowerUp):
    reward_points = 10
    sprite = pygame.image.load("assets/Health_PUP.png")

    def __init__(self, *args, **kwargs):
        # load the image for the base class.
        self._base_image = HealthPowerUp.sprite

        super().__init__(*args, **kwargs)

    def _consume(self, consumer):
        consumer.increment_health(self.reward_points) 
