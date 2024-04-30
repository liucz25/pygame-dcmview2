from .imgprocessfunction import ImgProcessFunction


import pygame

from ..manager.dcmmanager import DcmManager


class ViewPic(ImgProcessFunction):
    def __init__(self, dcmmanager) -> None:
        super().__init__(dcmmanager)
        self.mstartx = 0
        self.mstarty = 0
        self.mstopx = 0
        self.mstopy = 0
        self.is_move = False
        self.changerate = 20




    def change_wwwl(self):
        if self.is_move:
            if self.dcm.ww > 0:
                self.dcm.wl += (self.mstopy-self.mstarty)/self.changerate
            else:
                self.dcm.wl -= (self.mstopy-self.mstarty)/self.changerate
            if (self.dcm.ww+((self.mstopx-self.mstartx)/self.changerate)) > 0:
                self.dcm.ww += (self.mstopx-self.mstartx)/self.changerate
            # print(self.dcm.ww, self.dcm.wl)
            # return self.dcm.ww, self.dcm.wl

    def function_mouse_down(self, event):

        self.mstartx, self.mstarty = event.pos
        self.is_move = True
        return self.wwwl2img()

    def function_mouse_move(self,  event):

        if self.is_move:
            self.mstopx, self.mstopy = event.pos
            self.change_wwwl()

        return self.wwwl2img()

    def function_mouse_up(self,  event):
        self.is_move = False

        return self.wwwl2img()

    def function_key_up(self, event):
        self.dcm.wl += 1

        return self.wwwl2img()

    def function_key_down(self, event):
        self.dcm.wl -= 1

        return self.wwwl2img()

    def function_key_right(self, event):
        self.dcm.ww += 1

        return self.wwwl2img()

    def function_key_left(self, event):
        self.dcm.ww -= 1

        return self.wwwl2img()

    def function_key_click(self, event):

        return self.wwwl2img()
    
