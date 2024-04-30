from .imgprocessfunction import ImgProcessFunction

import numpy as np
import cv2 as cv


class SiftPic(ImgProcessFunction):
    def function_key_click(self, event):

        sift = cv.SIFT_create()
        kp = sift.detect(self.dcm.saveimg, None)
        out=np.zeros((512,512,3),np.uint8)
        img = cv.drawKeypoints(self.dcm.saveimg,kp,out)
        cv.imwrite("sift_out.png",out)
        cv.imwrite("sift_img.png",img)
        cv.imwrite("sift_dcm_img.png",self.dcm.saveimg)
        
        return img
