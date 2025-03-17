import pygame
import sys

# 初始化Pygame
pygame.init()

# 创建800x600的窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("键盘事件检测")

# 主循环标志
running = True

while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 点击关闭按钮时退出
        elif event.type == pygame.KEYDOWN:
            # 打印按键的原始键值（整数）和对应的键名
            print(f"按下的键值：{event.key} → 对应键名：{pygame.key.name(event.key)}")

    # 更新屏幕显示
    pygame.display.flip()

# 退出程序
pygame.quit()
sys.exit()
