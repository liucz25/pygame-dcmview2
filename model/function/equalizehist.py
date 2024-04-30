from .imgprocessfunction import ImgProcessFunction

import numpy as np
import cv2 as cv
# 一下为图像处理函数


class EqualizeHist(ImgProcessFunction):

    def function_key_click(self, event):
        # img = self.img[0].astype(np.uint8)
        # pixel = self.dcm.get_setDicomWinWidthWinCenter()
        # pixel = np.swapaxes(pixel, 0, 1)
        # cv.imshow("",pixel)
        # gray=cv.cvtColor(pixel,cv.COLOR_BGR2GRAY)
        # out = cv.equalizeHist(pixel)
        # cv.imwrite("e.png",out)
 
        (b,g,r)=cv.split(self.img)
        out=cv.equalizeHist(b)
        gray=cv.merge((out,out,out))
        # self.dcm.saveimg=gray
        return gray
