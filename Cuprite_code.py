#%%############## Import Libraries ##############%%#

import scipy.io
import numpy as np
from spectral import *
import matplotlib.pyplot as plt

#%%############## Read Hyperspectral Dataset ##############%%#

mat = scipy.io.loadmat(r"D:\Hyperspectral_dataset_Pavia\Cuprite.mat")
mat.keys()
data=mat['X']
print(f'The size of the hypersepctral image is ')
print(mat['X'].shape)
row,column,bands=mat['X'].shape
imshow(data, (16, 100, 180))

#%%############## Display the three bands of the HSI ##############%%#

plt.imshow(data[:,:,0],cmap=plt.cm.gray)
plt.title("1st band of the hyperspectral image")

#%% 
plt.imshow(data[:,:,9],cmap=plt.cm.gray)
plt.title("10th band of the hyperspectral image") 
#%%
plt.imshow(data[:,:,29],cmap=plt.cm.gray)
plt.title("30th band of the hyperspectral image") 


#%%################ Plot the spectral responses ###################

x = [k for k in range(1,bands+1)] # for no of bands from 1 to 103
img = data[50,50,:]
plt.plot(x,img,label='Reflectance values at [50,50]',color='blue', linewidth = 2, 
         marker='o', markerfacecolor='red', markersize=3)

plt.title('Spectral Response')
plt.xlabel('Bands number')
plt.ylabel('Reflectance')
plt.legend()
plt.show()