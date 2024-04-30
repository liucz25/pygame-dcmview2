from . import dcmlib
import pydicom
import matplotlib.pyplot as plt
import numpy
# import numpy as np
# import cv2
from PIL import Image



from matplotlib.colors import ListedColormap
from matplotlib import cm


def get_pixel_from_file(file):
    # file = file
    ds = pydicom.dcmread(file)
    return dcmlib.get_pixeldata(ds)

def get_wwwl_from_file(file):
    ds = pydicom.dcmread(file)
    return ds.WindowCenter,ds.WindowWidth

# 调整CT图像的窗宽窗位


def setDicomWinWidthWinCenter(img_data, winwidth, wincenter, rows, cols):
    img_temp = numpy.array(img_data)
    # print(type(img_temp))
    # print(type(img_data))
    img_temp.flags.writeable = True
    min = (2 * wincenter - winwidth) / 2.0 + 0.5
    max = (2 * wincenter + winwidth) / 2.0 + 0.5
    dFactor = 255.0 / (max - min)
    for i in numpy.arange(rows):
        for j in numpy.arange(cols):
            img_temp[i, j] = int((img_temp[i, j]-min)*dFactor)
    min_index = img_temp < 0
    img_temp[min_index] = 0
    max_index = img_temp > 255
    img_temp[max_index] = 255
    return img_temp.astype(numpy.uint8)


def setFanSigmaWinWidthWinCenter(img_data, winwidth, wincenter, rows, cols):
    img_temp = img_data
    # print(type(img_temp))
    # print(type(img_data))
    # img_temp.flags.writeable = True
    min = (2 * wincenter - winwidth) / 2.0 + 0.5
    max = (2 * wincenter + winwidth) / 2.0 + 0.5
    mid = (min+max)/2
    dFactor = 255.0 / (max - min)*2
    for i in numpy.arange(rows):
        for j in numpy.arange(cols):
            if (img_temp[i, j]-mid) > 0:
                img_temp[i, j] = int((img_temp[i, j]-mid)*dFactor)
            else:
                img_temp[i, j] = int((max-img_temp[i, j])*dFactor)
    min_index = img_temp < 0
    img_temp[min_index] = 255
    max_index = img_temp > 255
    img_temp[max_index] = 255
    return img_temp.astype(numpy.uint8)


def setSigmaWinWidthWinCenter(img_data, winwidth, wincenter, rows, cols):
    img_temp = img_data
    img_temp.flags.writeable = True
    min = (2 * wincenter - winwidth) / 2.0 + 0.5
    max = (2 * wincenter + winwidth) / 2.0 + 0.5
    mid = (min+max)/2
    dFactor = 255.0 / (max - min)*2
    for i in numpy.arange(rows):
        for j in numpy.arange(cols):
            if (img_temp[i, j]-mid) > 0:
                img_temp[i, j] = int((img_temp[i, j]-mid)*dFactor)
            else:
                img_temp[i, j] = int((max-img_temp[i, j])*dFactor)
    min_index = img_temp < 0
    img_temp[min_index] = 0
    max_index = img_temp > 255
    img_temp[max_index] = 0
    return img_temp.astype(numpy.uint8)


def gray(im):  # 转灰度，三通道都是 灰度值
    im = 255 * (im / im.max())
    w, h = im.shape
    ret = numpy.empty((w, h, 3), dtype=numpy.uint8)
    ret[:, :, 2] = ret[:, :, 1] = ret[:, :, 0] = im
    return ret


# save function

def save_im(pixel):

    image = Image.fromarray(pixel)
    image.save("wwwlok.jpg")


def use_less_now():
    top = cm.get_cmap('gray', 128)
    bottom = cm.get_cmap('binary', 128)

    newcolors = numpy.vstack((top(numpy.linspace(0, 1, 128)),
                              bottom(numpy.linspace(0, 1, 128))))
    # segema 窗
    newcmp = ListedColormap(newcolors, name='segema')
    file = 'ct_13.dcm'
    img, row, col = get_pixel_from_file(file)
    img2 = setDicomWinWidthWinCenter(img, 80, 40, row, col)
    img3 = setDicomWinWidthWinCenter(img, 160, 80, row, col)
    plt.subplot(221)
    im = plt.imshow(img3, cmap=newcmp)
    # print(im)
    plt.subplot(222)
    plt.imshow(img2, cmap='binary')
    plt.subplot(223)
    plt.imshow(img2, cmap='gray')
    # blur = cv2.blur(img3, (3, 3),)
    # plt.imshow(blur, cmap=newcmp)
    # plt.imshow(im, cmap='gray')
    plt.show()


if __name__ == '__main__':
    use_less_now()
