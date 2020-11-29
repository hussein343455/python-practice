#read abd show an img
from matplotlib import pyplot as plt
from PIL import Image
import  numpy as np

img = Image.open('ss.jpg')
img_np=np.array(img)
plt.imshow(img_np)
plt.show()