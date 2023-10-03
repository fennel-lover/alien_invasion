import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()
        # 赋给属性self.screen 的对象是一个surface。
        # 在Pygame中，surface是屏幕的一部分，用于显示游戏元素。
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件。
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #每次循环时都重绘屏幕。
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # 让最近绘制的屏幕可见。
            pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()