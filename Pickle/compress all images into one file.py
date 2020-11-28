import pickle
import cv2
import glob
path="cats/cat*"
# initialize the list of images
images = []
for i in glob.glob(path):
  image = cv2.imread(i)
  image=cv2.resize(image,(64,64))#resize all files/images to save space
  images.append(image)

#compress file
f=open("cat_images.p", "wb")
pickle.dump(images,f )
f.close()

#read file
filex = open("cat_images.p",'rb')
images2 = pickle.load(filex)
filex.close()