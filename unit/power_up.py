import pygame
from unit.base_unit import BaseUnit

SIZE = 20

class PowerUp(BaseUnit):
    reward = None
    reward_points = 0
    team = 2 # Since we do not have a known team
    def __init__(self, *args, **kwargs):
        self.max_atk_range = 0
        super().__init__(health=self.reward_points, *args, **kwargs)

    def consume(self):
        return self.reward, self.reward_points

    def hurt(self, damage):
        pass
