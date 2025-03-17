import pygame
from pygame.sprite import Sprite						#在 Pygame 中，pygame.sprite.Sprite 是创建和管理游戏精灵（如角色、子弹等动态元素）的核心基类。

class Bullet(Sprite):
	"""一个对飞船发射的子弹进行管理的类"""
	def __init__ (self,ai_settings,screen,ship):
		"""在飞船所处的位置创建一个子弹对象"""
		super(). __init__ ()
		self.screen = screen
		
		''' 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置'''
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx			#将子弹x中心设置在飞船中心处
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)						#我们将子弹的y坐标存储为小数值，以便能够微调子弹的速度
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""向上移动子弹"""
		self.y -= self.speed_factor
		self.rect.y = self.y							#更新表示子弹的rect的位置
		
		
	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)	#pygame.draw.rect 是 Pygame 中用于绘制矩形的核心函数，支持实心填充或边框样式的绘制。
