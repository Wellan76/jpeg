import matplotlib.image as mpimag
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy import misc

M =mpimag.imread('Marcel Sembat.png')
imageA=mpimag.imread('Marcel Sembat.png')
plt.imshow(imageA, interpolation='nearest')
plt.axis('off')
plt.show()
taille =M.shape
P=taille[0]
M=taille[1]

imageB=np.zeros((16,16,3))
for y in range(0,16):
    for x in range(0,16):
        imageB[x,y]=imageA[x,y]
print(imageB)

imageC=np.zeros((16,16,3))
for y in range(0,16):
    for x in range(16,32):
        imageC[x-16,y]=imageA[x,y]
print(imageC)


plt.imshow(imageB, interpolation='nearest')
plt.axis('off')
plt.show()
plt.imshow(imageC, interpolation='nearest')
plt.axis('off')
plt.show()


print(taille)
print(P)
print(M)
print("fin")
