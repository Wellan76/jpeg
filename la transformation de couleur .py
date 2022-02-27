import matplotlib.image as mpimag
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

imageA=mpimag.imread('Marcel Sembat.png')
plt.imshow(imageA, interpolation='nearest')
plt.axis('off')
plt.show()

imagemichelle=np.zeros((587,1020,3))
for y in range(1020):
    for x in range(587):
        imagemichelle[x,y]=imageA[x,y]
print(imagemichelle)



img=Image.open('Marcel Sembat.png')
largeur_image=10
hauteur_image=5
imageb=np.zeros((587,1020,3))
for y in range(1020):
    for x in range(587):
        """r,v,b=img.getpixel((x,y))"""


        Y  = imagemichelle[x,y,0] *  0.29900 + imagemichelle[x,y,1] *  0.58700 + imagemichelle[x,y,2] *  0.11400
        Cb = imagemichelle[x,y,0] * -0.16874 + imagemichelle[x,y,1] * -0.33126 + imagemichelle[x,y,2] *  0.50000 + 128
        Cr = imagemichelle[x,y,0] *  0.50000 + imagemichelle[x,y,1] * -0.41869 + imagemichelle[x,y,2] * -0.08131 + 128

        imageb[x,y,0]=Y
        imageb[x,y,1]=Cb
        imageb[x,y,2]=Cr


plt.imshow(imageb, interpolation='nearest')
plt.axis('off')
plt.show()

print("fin")

