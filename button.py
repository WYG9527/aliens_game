import pygame.font														#我们导入了模块pygame.font，它让Pygame能够将文本渲染到屏幕上。

class Button():
	def __init__(self,ai_settings,screen,msg):
		"""初始化按钮的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# 设置按钮的尺寸和其他属性
		self.width,self.height = 200,50
		self.button_color = (86,152,195)
		self.text_color = (255,255,255)
		self.font = pygame.font.Font("fonts\龚帆霸道体.ttf",48)						#我们指定使用什么字体来渲染文本。实参None让Pygame使用默认字体，而48指定了文本的字号。
		
		self.rect = pygame.Rect(0,0,self.width,self.height)				#创建一个矩形对象,这里 (0, 0) 表示矩形的左上角坐标。后续通常会通过 center 或 centerx/centery 等属性调整位置。
		self.rect.center = self.screen_rect.center
		# 按钮的标签只需创建一次
		self.prep_msg(msg)

	def prep_msg(self,msg):
		"""将msg渲染为图像，并使其在按钮上居中"""
		self.msg_image = self.font.render(msg,True,self.text_color,
			self.button_color)
		'''​msg要渲染的文本内容，可以是字符串或 Unicode。例如 "Play" 表示按钮标签。若为空字符串，会生成一个空白图像。
			True控制是否启用抗锯齿​。设置为 True 时，文本边缘平滑，视觉效果更佳（如 Webpage 1 和 4 中描述的按钮文本渲染）；
			设置为 False 时，文本边缘可能呈现锯齿状，但渲染速度更快。**self.text_color**文本颜色，通常以 RGB 元组表示（如 (255, 255, 255) 为白色）。颜色直接影响文本的视觉表现。
			​**self.button_color**文本背景色，可选参数。若指定，文本将填充该颜色（如绿色按钮背景 (0, 255, 0)）；若为 None，背景透明。'''
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# 绘制一个用颜色填充的按钮，再绘制文本
		self.screen.fill(self.button_color,self.rect)					#fill() 是用于填充 Surface 对象（通常是游戏窗口）背景色的核心方法
		self.screen.blit(self.msg_image,self.msg_image_rect)			
		

		
