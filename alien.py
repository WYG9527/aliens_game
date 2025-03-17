import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	def __init__ (self,ai_settings,screen):
		super().__init__ ()
		self.ai_settings = ai_settings
		self.screen = screen
		
		# 加载外星人图像，并设置其rect属性
		original_image = pygame.image.load('images/alien.png')
		new_width=original_image.get_width()//2							#在 Pygame 中缩小飞船图片的核心方法是使用 pygame.transform.scale() 或 pygame.transform.smoothscale()
		new_height=original_image.get_height()//2
		self.image = pygame.transform.smoothscale(original_image, (new_width, new_height))
		
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width									#表示将当前对象的水平坐标设置为等于其自身宽度。例如：若外星人宽度为 60px，则其初始 x 坐标为 60px，避免紧贴屏幕左边缘
		self.rect.y = self.rect.height									#同理
		
		self.x = float(self.rect.x)										# 存储外星人的准确位置
		
	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image,self.rect)
		
	def check_edges(self):
		"""如果外星人位于屏幕边缘，就返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		
		elif self.rect.left <= 0:
			return True
		
		
	def update(self):
		"""向左或向右移动外星人"""
		self.x += (self.ai_settings.alien_speed_factor * 
						self.ai_settings.fleet_direction)
		self.rect.x = self.x
