import pydicom
# import numpy
# from model.tool import dcmtool

# # ds1=dcmtool.get_pixel_from_file("./dcm/ct_01.dcm")
# # ds2=dcmtool.get_pixel_from_file("./dcm/ct_02.dcm")
# # print(type(ds1))
# # dp1=numpy.array(ds1)
# # dp2=numpy.array(ds2)
# # print(dp1)
# # # dt1=dcmtool.setFanSigmaWinWidthWinCenter(dp1,2000,800,512,512)
# # dt1=dcmtool.setDicomWinWidthWinCenter(dp1,2000,800,512,512)
# pixel=[]
# pixel=dcmtool.get_pixel_from_file("./dcm/ct_01.dcm")
# pixel2 = dcmtool.setDicomWinWidthWinCenter(pixel,2000,800,512,512)




from model.tool import dcmlib
from model.tool import dcmtool
import matplotlib.pyplot as plt

file1 = './dcm2/1.dcm'
file2='./dcm2/2.dcm'
pixel1, row, col = dcmtool.get_pixel_from_file(file1)
pixel2, row, col = dcmtool.get_pixel_from_file(file2)
ds1=pydicom.dcmread(file1)
ds2=pydicom.dcmread(file2)
print(ds1.WindowWidth,ds1.WindowCenter)
print(ds2.WindowWidth,ds2.WindowCenter)
img1=dcmtool.setDicomWinWidthWinCenter(pixel1,ds1.WindowWidth,ds1.WindowCenter,row,col)
img2=dcmtool.setDicomWinWidthWinCenter(pixel2,ds1.WindowWidth,ds1.WindowCenter,row,col)

img3=img1-img2
plt.imshow(img3,cmap='gray')
plt.show()