from unit.water_unit import WaterUnit
import unit, helper, effects
from tiles import Tile
import pygame

class PT_boat(WaterUnit):
	"""
	A small, fast and manuverable boat. Less fire power and health than
	over water units, but can get around easier.
	
	Armour: LOW
	Speed: VERY HIGH
	Attack Range: HIGH
	Damage: Medium
	"""
	sprite = pygame.image.load("assets/PT-boat.png")
	
	def __init__(self, **keywords):
		# load the image for the pt_boat
		self._base_image = PT_boat.sprite
		
		# loads the base class
		super().__init__(**keywords)
		
		# sets the sounds
		self.hit_sound = "ArtilleryFire"
		
		# set unit attributes
		self.type = "PT-Boat"
		self.speed = 12
		self.max_atk_range = 6
		self.damage = 4
		self.defense = 1
		self.hit_effect = effects.Explosion

		self.health = 12
		self.max_health = self.health

		self._update_image()

unit.unit_types["PT-Boat"] = PT_boat
