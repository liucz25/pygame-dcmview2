from model.tool import dcmlib
from model.tool import dcmtool
import matplotlib.pyplot as plt

file1 = 'ct_14.dcm'
file2='ct_15.dcm'
pixel1, row, col = dcmtool.get_pixel_from_file(file1)
pixel2, row, col = dcmtool.get_pixel_from_file(file2)
img1=dcmtool.setDicomWinWidthWinCenter(pixel1,80,40,row,col)
img2=dcmtool.setDicomWinWidthWinCenter(pixel2,80,40,row,col)

img3=img2-img1
plt.imshow(img3,cmap='gray')
plt.show()