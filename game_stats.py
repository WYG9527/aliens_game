


class GameStats():
	"""跟踪游戏的统计信息"""
	def __init__(self,ai_settings):
		self.ai_settings = ai_settings
		self.rect_stats()
		
	def rect_stats(self):
		'''在这个游戏运行期间，我们只创建一个GameStats实例，但每当玩家开始新游戏时，需要重
		置一些统计信息。为此，我们在方法reset_stats()中初始化大部分统计信息，而不是在__init__()
		中直接初始化它们。我们在__init__()中调用这个方法，这样创建GameStats实例时将妥善地设置
		这些统计信息，同时在玩家开始新游戏时也能调用reset_stats()。'''
		self.ships_left = self.ai_settings.ship_limit
