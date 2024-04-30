import pygame


class PygameManager():
    def __init__(self) -> None:
        self.surface = []
        self.screen = ''

    def img2surface(self, im):

        return pygame.surfarray.make_surface(im)

    def show_ww_wl(self, screen, ww, wl):
        # 显示文字
        font = pygame.font.Font("Font/HYSongYunLangHeiW-1.ttf", 15)
        s = 'ww:{0:.0f} wl:{1:.0f}'.format(ww, wl)
        # print(s)
        text = font.render(s, True, (205, 85, 85), (240, 225, 240))
        w, h = text.get_size()
        screen.blit(text, (512-w, 512-h))

    def refresh(self, screen, img, ww, wl):
        self.screen = screen
        self.surface = self.img2surface(img)
        self.screen.blit(self.surface, (0, 0))
        self.show_ww_wl(self.screen, ww, wl)

    def showkey(self, event):
        print("-"*20, event.key, event)
