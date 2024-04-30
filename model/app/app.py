# pygamed 的封装 把pygame封装成事件循环

# 导入所需的模块
from random import randint
import sys
import pygame


class APP():
    def __init__(self, app_event):
        self.app_event = app_event
        self.fps = 60
        self.fcclock = pygame.time.Clock()
        # 使用pygame之前必须初始化
        pygame.init()

        # 设置主屏窗口
        self.screen = pygame.display.set_mode((512, 512))

        # 设置窗口的标题，即游戏名称
        pygame.display.set_caption('hello world')

    def mainloop(self):
        while True:
            # 循环获取事件，监听事件状态
            for event in pygame.event.get():
                # 判断用户是否点了"X"关闭按钮,并执行if代码段
                if event.type == pygame.QUIT:
                    # 卸载所有模块
                    pygame.quit()
                    # 终止程序，确保退出程序
                    sys.exit()
                self.app_event.eventloop(self.screen, event)
            self.fcclock.tick(self.fps)
        pygame.display.flip()  # 更新屏幕内容

    def run(self):
        # self.init()
        self.mainloop()
