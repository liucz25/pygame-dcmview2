from .viewpic import ViewPic

from ..manager.dcmmanager import DcmManager


class SigmaPic(ViewPic):
    # def __init__(self, dcmmanger) -> None:
    #     super().__init__(dcmmanger)
    #     # self.img = self.wwwl2img()

    def wwwl2img(self):

        pixel = self.dcm.get_setSigmaWinWidthWinCenter()
        self.img=self.dcm.img=self.dcm.saveimg = self.dcm.pixel2img(pixel)
        return self.img
