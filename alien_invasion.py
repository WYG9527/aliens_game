import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def run_game(): 
	pygame.init()										#初始化背景设置，让Pygame能够正确地工作。
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))			#创建一个显示窗口，这个游戏的所有图形元素都将在其中绘制。实参(1200, 800)，指定了游戏窗口的尺寸。创建了一个宽1200像素、高800像素的游戏窗口.
	pygame.display.set_caption('打外星人小游戏')			#调用的是set_caption方法，设置窗口的标题为“Alien Invasion”。这会让游戏窗口的标题栏显示这个标题，方便用户识别。
	'''创建一个用于存储游戏统计信息的实例'''
	stats = GameStats(ai_settings)
	'''创建一艘飞船、一个子弹编组和一个外星人编组'''
	ship = Ship(ai_settings,screen)
	alien = Alien(ai_settings,screen)
	bullets = Group()									#创建一个用于存储子弹的编组
	aliens = Group()
	
	gf.create_fleet(ai_settings,screen,ship,aliens)			#创建外星人群
	
	'''游戏主循环'''
	while True:											#为让程序响应事件，我们编写一个事件循环，以侦听事件，并根据发生的事件执行相应的任务。
		'''我们将bullets传递给了check_events()和update_screen()。在check_events()中，需要在玩
			家按空格键时处理bullets；而在update_screen()中，需要更新要绘制到屏幕上的bullets。
			当你对编组调用update()时，编组将自动对其中的每个精灵调用update()，因此代码行
			bullets.update()将为编组bullets中的每颗子弹调用bullet.update()。'''
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
		gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		gf.update_screen(ai_settings,stats,screen,ship,aliens,bullets)
							
run_game()
