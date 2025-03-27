class Settings():
	"""存储《外星人入侵》的所有设置的类"""
	def __init__ (self):
		"""初始化游戏的静态设置""" 
		self.screen_width=1000				# 屏幕设置
		self.screen_height=750
		self.bg_color=(255,255,255)			#背景颜色
		'''飞船参数'''
		self.ship_limit = 3
		'''子弹参数'''
		self.bullet_width = 15
		self.bullet_height = 15
		self.bullet_color = (99,187,208)
		self.bullets_allowed = 3000
		
		self.fleet_drop_speed = 16			#设置fleet_drop_speed指定了有外星人撞到屏幕边缘时，外星人群向下移动的速度。将这个速度与水平速度分开是有好处的，这样你就可以分别调整这两种速度了。
		self.speedup_scale = 1.2			# 以什么样的速度加快游戏节奏
		self.score_scale = 1.5				# 外星人点数的提高速度
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而变化的设置"""
		self.ship_speed_factor = 1.5		#飞创移动速度
		self.bullet_speed_factor = 1
		self.alien_speed_factor = 0.1
		
		self.fleet_direction = 1			# fleet_direction为1表示向右移，为-1表示向左移
		# 记分
		self.alien_points = 50
		
	def increase_speed(self):
		"""提高速度设置"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		
