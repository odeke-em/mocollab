import pygame

from unit.power_up import PowerUp

class AttackPowerUp(PowerUp):
    reward_points = 2
    sprite = pygame.image.load("assets/Damage_PUP.png")

    def __init__(self, *args, **kwargs):
        # load the image for the base class.
        self._base_image = AttackPowerUp.sprite

        super().__init__(*args, **kwargs)

    def _consume(self, consumer):
        # Task 2: Clause 3 expectation, if of Transport type, pick it but
        #         do not affect the transport
        if consume.type != "Transport":
            consumer.increment_damage(self.reward_points) 
