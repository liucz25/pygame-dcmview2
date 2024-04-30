# 事件循环的父类，实现事件的封装，扩展时继承该类，在该类中的列表中添加字符串，在子类中实现同名的方法，实现扩展功能
# 如果有必要添加一个字典，记录动作和功能的关系，添加一个管理类管理这些
from ..manager.pygamemanager import PygameManager
from ..manager.eventmanager import EventManager
from ..manager.dcmmanager import DcmManager
import pygame


class MyEvent(object):
    def __init__(self) -> None:
        #     self.mouse_event = MouseEvent()
        #     self.key_event = KeyEvent()
        self.dcmmanager = DcmManager()
        self.eventmanager = EventManager(self.dcmmanager)
        self.pygamemanager = PygameManager()

    def eventloop(self, screen, event):
        self.eventmanager.bind_event(event)
        img = self.eventmanager.get_img(event)
        ww, wl = self.eventmanager.get_ww_wl()
        self.pygamemanager.refresh(screen, img, ww, wl)
        pygame.display.update()
