import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__ (self,ai_settings,screen):						#screen将指定要将飞船绘制到什么地方。ai_settings为Settings的一个实例。
		super().__init__()
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings				
		# 加载飞船图像并获取其外接矩形
		self.original_image = pygame.image.load('images/ship.png')	#为加载图像，我们调用了pygame.image.load()。这个函数返回一个表示飞船的surface，而我们将这个surface存储到了self.image中。
		'''该函数从指定路径加载图像文件（如 PNG、JPG、BMP 等），将其转换为 Pygame 的 Surface 对象。Surface 对象是 Pygame 中表示图像的基础数据结构，支持后续的绘制、变换等操作'''
		
		self.new_width=self.original_image.get_width()//4					#在 Pygame 中缩小飞船图片的核心方法是使用 pygame.transform.scale() 或 pygame.transform.smoothscale()
		self.new_height=self.original_image.get_height()//4
		self.image = pygame.transform.smoothscale(self.original_image, (self.new_width, self.new_height)) 
		
		self.rect = self.image.get_rect()						#我们使用get_rect()获取相应surface的属性rect
		self.screen_rect = screen.get_rect()					#首先将表示屏幕的矩形存储在self.screen_rect中
		
		self.rect.centerx = self.screen_rect.centerx			#将游戏对象的水平中心位置与屏幕的水平中心对齐,self.rect 是游戏对象（如按钮、飞机）的矩形区域，self.screen_rect 是屏幕的矩形区域。centerx 属性表示矩形的水平中心坐标。通过将游戏对象的 centerx 赋值为屏幕的 centerx，可实现对象的水平居中。
		self.rect.bottom = self.screen_rect.bottom				#将游戏对象的底部边缘与屏幕的底部边缘对齐。
		self.center = float(self.rect.centerx)
		
		self.botto = float(self.rect.bottom)					#上
		
		self.moving_right = False								#飞船不动时，标志moving_right将为False。玩家按下右箭头键时，我们将这个标志设置为True；而玩家松开时，我们将这个标志重新设置为False。
		self.moving_left = False								#同上
		
		self.moving_up = False									#上
		self.moving_down = False

	def update(self):
		"""根据移动标志调整飞船的位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:	#我们添加了方法update()，它在前述标志为True时向右移动飞船。
			self.center += self.ai_settings.ship_speed_factor
			
		if self.moving_left and self.rect.left > 0:							#向左移动
			self.center -= self.ai_settings.ship_speed_factor
			
		if self.moving_up and self.rect.top > 0:							#上
			self.botto -= self.ai_settings.ship_speed_factor
			
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:	#下
			self.botto += self.ai_settings.ship_speed_factor
			
		
		
		self.rect.centerx = self.center							# 根据self.center更新rect对象
		self.rect.bottom = self.botto
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)					# 是用于将图像绘制到屏幕上的核心方法
		'''blit() 是 Pygame 中用于将一个 Surface 对象（图像）绘制到另一个 Surface（通常是屏幕）上的方法。
			self.image 是待绘制的图像对象（如飞船、按钮等），通过 pygame.image.load() 加载生成。
			self.rect 是图像对应的矩形区域对象（Rect 类），存储了图像的尺寸和位置信息（如左上角坐标 (x, y)、中心点 centerx 等）。
			这行代码的实际效果是将 self.image 绘制到 self.screen 的指定位置，位置由 self.rect 的坐标属性决定。'''

	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.center = self.screen_rect.centerx
		self.botto = self.screen_rect.bottom
		
		
