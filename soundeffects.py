import pygame

class Sound():
	'''存储音效相关的类'''
	def __init__(self):
		self.shoot_sound = pygame.mixer.Sound("sound/shoot.mp3")
		self.alien_hit = pygame.mixer.Sound("sound/alien.mp3")
		self.bj_sound = pygame.mixer.Sound("sound/bjyy.mp3")
		
