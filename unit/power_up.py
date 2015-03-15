import pygame
from unit.base_unit import BaseUnit

SIZE = 20

class PowerUp(BaseUnit):
    reward_points = 0
    team = 2 # Since we do not have a known team
    def __init__(self, *args, **kwargs):
        self.max_atk_range = 0
        super().__init__(health=self.reward_points, consumable=True, *args, **kwargs)

    def consume(self, consumer):
        self._consume(consumer)
        self.deactivate()
        consumer._update_image()

    def _consume(self, consumer):
        pass
