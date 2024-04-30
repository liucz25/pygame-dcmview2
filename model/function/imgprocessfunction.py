# from function.funclist import FunctList
from abc import abstractmethod, ABCMeta

from ..tool.ostool import get_fileList_from_dir_string

class ImgProcessFunction(metaclass=ABCMeta):
    # 图像处理基类
    # 约定图像处理的接口，当鼠标down up move 还有键盘上下左右时的抽象方法名称
    def __init__(self, dcmmanager) -> None:
        self.dcm = dcmmanager
        self.getwwwl()
        self.img = self.dcm.img
        
        self.file_list=get_fileList_from_dir_string()
        self.file_no=0
 
        self.dcm.file=self.file_list[self.file_no]
        # self.wwwl2img()

    def getwwwl(self):
        return self.dcm.ww, self.dcm.wl  # 以后改

    def wwwl2img(self):
        pixel = self.dcm.get_setDicomWinWidthWinCenter()
        self.img=self.dcm.img=self.dcm.saveimg = self.dcm.pixel2img(pixel)
        return self.img

    @abstractmethod
    def function_key_click(self, event):
        pass

    # @abstractmethod #如果是抽象方法，子类必须实现，这个不必须
    def function_mouse_down(self, event):
        return self.img

    # @abstractmethod  # 如果是抽象方法，子类必须实现，这个不必须
    def function_mouse_up(self, event):
        return self.img

    # @abstractmethod  # 如果是抽象方法，子类必须实现，这个不必须
    def function_mouse_move(self, event):
        return self.img

    def function_key_up(self, event):
        return self.img

    def function_key_down(self, event):
        return self.img

    def function_key_right(self, event):
        return self.img

    def function_key_left(self, event):
        return self.img
    def function_key_pageup(self, event):
        return self.img
    def function_key_pagedown(self, event):
        return self.img
    
    def function_key_click_updata(self,event):
        if not self.dcm.saveimg==[]:
            self.img=self.dcm.saveimg
        self.dcm.saveimg=self.function_key_click(event)
        return self.dcm.saveimg     
    
    
    def function_key_pageup(self, event):
        if self.file_no>0:
            self.file_no-=1
        self.dcm.file=self.file_list[self.file_no]
        return self.wwwl2img()
        

    def function_key_pagedown(self, event):
        if self.file_no<len(self.file_list):
            self.file_no+=1
        self.dcm.file=self.file_list[self.file_no]
        return self.wwwl2img()