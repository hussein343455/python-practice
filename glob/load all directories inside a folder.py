import glob
import cv2

path="cats/cat*"
images = []
for i in glob.glob(path):
  image = cv2.imread(i)
  images.append(image)

print(images.shape)
