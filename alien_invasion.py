import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
    
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, events):
        """响应按键"""
        if events.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif events.key ==pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif events.key == pygame.K_SPACE:
            # 空格发射子弹
            self._fire_bullet()
        elif events.key == pygame.K_q:
            # 按q退出
            sys.exit()
    
    def _check_keyup_events(self, events):
        """响应松开"""
        if events.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif events.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中。"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹位置并删除消失的子弹"""
        # 更新子弹位置。
        self.bullets.update()

        # 删除消失的子弹。
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        #每次循环时都重绘屏幕。
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见。
        pygame.display.flip()



if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()