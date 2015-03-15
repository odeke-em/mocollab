import pygame
from unit.base_unit import BaseUnit

SIZE = 20

class PowerUp(BaseUnit):
    team = 0 # Since we do not have a known team
    reward_points = 0
    def __init__(self, *args, **kwargs):
        self.max_atk_range = 2
        super().__init__(*args, **kwargs)
