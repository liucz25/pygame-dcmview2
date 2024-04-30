from ..tool import dcmtool
import numpy


class DcmManager():
    def __init__(self) -> None:


        self.row = 0
        self.col = 0
        self.raw_pixel = []

        self.file = 'ct_13.dcm'
        self.img = []
        self.saveimg=[]
        self.get_ww_wl()
        
        
    def get_ww_wl(self):
        self.wl ,self.ww = dcmtool.get_wwwl_from_file(self.file)
        
    def get_raw_pixel(self):
        self.raw_pixel, self.row, self.col = dcmtool.get_pixel_from_file(
            self.file)
        return self.raw_pixel

    def get_setDicomWinWidthWinCenter(self):
        pixel = self.get_raw_pixel()
        pixel = dcmtool.setDicomWinWidthWinCenter(
            self.raw_pixel, self.ww, self.wl, self.row, self.col)
        # pixel = dcmtool.setFanSigmaWinWidthWinCenter(img, ww, wl, row, col)
        return pixel

    def get_setSigmaWinWidthWinCenter(self):
        pixel = self.get_raw_pixel()
        # pixel = dcmtool.setDicomWinWidthWinCenter(self.raw_pixel, self.ww, self.wl, self.row, self.col)
        pixel = dcmtool.setSigmaWinWidthWinCenter(
            self.raw_pixel, self.ww, self.wl, self.row, self.col)
        return pixel

    def pixel2img(self, pixel):
        pixel = numpy.swapaxes(pixel, 0, 1)
        self.img = dcmtool.gray(pixel)
        return self.img

    def set_ww_wl(self, ww, wl):
        self.ww = ww
        self.wl = wl

    def set_file_name(self, file_name):
        self.file = file_name
