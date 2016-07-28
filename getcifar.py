import cv2
import scipy.io as sio
import numpy as np

mat = sio.loadmat('data_batch_5.mat')
label = mat['labels']
data = mat['data']

for index in range(0,10000):
  pic = np.array(data[index])
  pic = np.resize(pic,(3,32,32))

  rgb = []

  for x in range(0,32):
    for y in range(0,32):
      mixer = pic[0][x][y], pic[1][x][y], pic[2][x][y],
      rgb.append(mixer)

  pic = np.array(rgb)
  pic = np.resize(pic,(32,32,3))

  if label[index] ==1 :
    a = cv2.imwrite('positive_images/carpic'+str(index)+'.bmp', pic)
    print(a)
  else:
    cv2.imwrite('negative_images/otherpic'+str(index)+'.bmp', pic)



