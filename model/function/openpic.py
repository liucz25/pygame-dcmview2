from .imgprocessfunction import ImgProcessFunction

import numpy as np
import cv2 as cv


class OpenPic(ImgProcessFunction):
    def function_key_click(self, event):
        
        if not self.dcm.saveimg==[]:
            self.img=self.dcm.saveimg
        k = np.ones((3, 3), np.uint8)
        op= cv.morphologyEx(self.img, cv.MORPH_OPEN, k)
        # self.dcm.saveimg=op
        return  op
