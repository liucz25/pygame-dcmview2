from .imgprocessfunction import ImgProcessFunction

import numpy as np
import cv2 as cv


class ClosePic(ImgProcessFunction):

    def function_key_click(self, event):  # 这个方法名应该是固定的 是基类的具体实现
        # if not self.dcm.saveimg==[]:
        #     self.img=self.dcm.saveimg
        k = np.ones((3, 3), np.uint8)
        cl = cv.morphologyEx(self.img, cv.MORPH_CLOSE, k)
        return cl
