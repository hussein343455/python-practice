import glob
import cv2
from imutils import build_montages
import matplotlib.pyplot as plt

path="dogs-vs-cats/train/train/*"
# initialize the list of images
images = []
for i in glob.glob(path):
  image = cv2.imread(i)
  images.append(image)
# construct the montages for the images

montages = build_montages(images[:8], (128, 192), (4, 2))


for montage in montages:
  plt.imshow(montage)
  plt.show()