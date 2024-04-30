# 先做按键绑定，然后再上下左右
# {"key_s":"siftpic","key_o":"openpic",....}
import pygame
# import dictmanager
# from tool import stringtool
# import importlib #动态加载 ，以后实现
from ..function.viewpic import ViewPic
from ..function.siftpic import SiftPic
from ..function.closepic import ClosePic
from ..function.openpic import OpenPic
from ..function.guussianpic import GuussianPic
from ..function.sigmapic import SigmaPic
from ..function.equalizehist import EqualizeHist


class EventManager(object):
    def __init__(self, dcmmanager) -> None:
        self.dcmmanager = dcmmanager
        self.rawdict = {"key_s": "siftpic", "key_o": "openpic",
                        "key_c": "closepic", "key_g": "guusianpic",
                        "key_v": "viewpic"}
        self.instance = ViewPic(dcmmanager)

        # self.current_key = None
    # def get_function(self,name): #动态加载，以后实现
    #         self.instance=self.rawdict.get(name)
    #         self.classname=stringtool.getClassName(self.instance)
    #         self.lujing=''
    #         clazz=importlib.import_module(module)
    #         return clazz.function_key_down
    def bind_event(self, event):  # 接受事件接口
        self.current_function = self.event_assign(event)

    def get_img(self, event):  # 返回图像接口
        if self.current_function:
            self.instance.img = self.current_function(event)
        else:

            self.current_function = self.instance.function_key_click
            self.instance.img = self.current_function(event)
        return self.instance.img

    def get_ww_wl(self):
        return self.instance.getwwwl()

    def key_event_assign(self, event):  # 键盘事件分派
        # 上下左右
        if event.key == pygame.K_UP:
            return self.instance.function_key_up
        elif event.key == pygame.K_DOWN:
            return self.instance.function_key_down
        elif event.key == pygame.K_RIGHT:
            return self.instance.function_key_right
        elif event.key == pygame.K_LEFT:
            return self.instance.function_key_left
        elif event.key == pygame.K_PAGEUP:
            return self.instance.function_key_pageup
        elif event.key == pygame.K_PAGEDOWN:
            return self.instance.function_key_pagedown
        # 功能键  以后可以动态加载
        elif event.key == pygame.K_s:
            self.instance = SiftPic(self.dcmmanager)
            return self.instance.function_key_click
        elif event.key == pygame.K_o:
            self.instance = OpenPic(self.dcmmanager)
            return self.instance.function_key_click_updata
        elif event.key == pygame.K_c:
            self.instance = ClosePic(self.dcmmanager)
            return self.instance.function_key_click_updata
        elif event.key == pygame.K_g:
            self.instance = GuussianPic(self.dcmmanager)
            return self.instance.function_key_click_updata
        elif event.key == pygame.K_v:
            self.instance = ViewPic(self.dcmmanager)
            return self.instance.function_key_click
        elif event.key == pygame.K_m:
            self.instance = SigmaPic(self.dcmmanager)
            return self.instance.function_key_click
        elif event.key == pygame.K_e:
            self.instance = EqualizeHist(self.dcmmanager)
            return self.instance.function_key_click_updata
        # 默认功能
        else:
            # self.instance = ViewPic()
            return self.instance.function_key_click

    def event_assign(self, event):  # 鼠标事件分派
        if event.type == pygame.KEYDOWN:
            return self.key_event_assign(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            return self.instance.function_mouse_down
        elif event.type == pygame.MOUSEBUTTONUP:
            return self.instance.function_mouse_up
        elif event.type == pygame.MOUSEMOTION:
            return self.instance.function_mouse_move
