import pygame.font												#在 Pygame 中，字体（font）的配置与文本渲染是实现界面交互的核心功能。
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	"""显示得分信息的类"""
	
	def __init__(self,ai_settings,screen,stats):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		# 显示得分信息时使用的字体设置
		self.text_color = (30,30,30)
		self.font = pygame.font.Font("fonts\龚帆霸道体.ttf",28)	#​字体设置，系统字体 SysFont(字体，字号)；使用自定义字体 Font(字体，字号)
		
		# 准备初始得分图像
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
		
	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		round_score = round(self.stats.score,-1)
		score_str = "{:,}".format(round_score)					#font.render() 方法仅接受字符串参数，直接传入整数会导致渲染错误
		self.score_image = self.font.render(score_str,True,self.text_color,
			self.ai_settings.bg_color)
		
		# 将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def prep_high_score(self):
		"""将最高得分转换为渲染的图像"""
		high_score = round(self.stats.high_score,-1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str,True,
			self.text_color,self.ai_settings.bg_color)
			
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
		
	def prep_level(self):
		"""将游戏等级转换为渲染的图像"""
		game_level = f"Lv：{self.stats.level}"
		self.level_image = self.font.render(game_level,True,
			self.text_color,self.ai_settings.bg_color)
		# 将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
	def prep_ships(self):
		"""显示还余下多少艘飞船"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings,self.screen)
			'''将飞船图片进一步缩小'''
			new_width=ship.original_image.get_width()//6	
			new_height=ship.original_image.get_height()//6
			ship.image = pygame.transform.smoothscale(ship.original_image, (new_width, new_height)) 
			ship.rect.x = 10 +ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
		
	def show_score(self):
		"""在屏幕上显示得分,游戏等级"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.ships.draw(self.screen)									# 绘制可用飞船
		
		
