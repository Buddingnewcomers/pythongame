class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255 ,255 , 255) #(255 ,255 , 255)

        # 飞船设置
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3  # 子弹数

        #外星人参数
        self.alien_speed = 1
        self.fleet_speed = 10

        self.fleet_direction = 1


