from .imgprocessfunction import ImgProcessFunction

import numpy as np
import cv2 as cv
# 一下为图像处理函数


class GuussianPic(ImgProcessFunction):

    def function_key_click(self, event):

        kernel_size = (5, 5)
        sigma = 5000
        blur = cv.GaussianBlur(self.img, kernel_size, sigma)

        return blur
