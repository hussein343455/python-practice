import cv2
import numpy as np

#----------------------------display image-----------------------------------------
# # img=cv2.imread('im.PNG')
# # cv2.imshow("output",img)
# # cv2.waitKey(1000)
# # cv2.destroyAllWindows()
#------------------------display a live video from cam----------------------------------------

# cap=cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# while True:
#     succ,img=cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) | 0XFF == ord('q'):
#         break
#--------------------------------resizing and image to 50% with some modifications--------------------------------------------
# img=cv2.imread('ss.jpg')
# width = int(img.shape[1] * 50 / 100)
# height = int(img.shape[0] * 50 / 100)
# dim = (width, height)
# img=cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
#
# imgG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgc=cv2.Canny(img,150,200)#make the img (7oaf zahra)
# imagDialation=cv2.dilate(imgc,np.ones((5,5),np.uint8),iterations=1)#dilate the edges
# imgErod=cv2.erode(imagDialation,np.ones((5,5),np.uint8),iterations=1)
#
# # cv2.imshow("gray",imgG)
# # cv2.imshow("imgc",imgc)
# cv2.imshow("imagDialation",imagDialation)
# cv2.imshow("imgErod",imgErod)
# cv2.waitKey(0)

#-----------------------crop an image ------------------------------
# img=cv2.imread('ss.jpg')
# imgcropp=img[500:800,400:900]
# cv2.imshow("imgcropp1",img)
# cv2.imshow("imgcropp",imgcropp)
# cv2.waitKey(0)

#----------------------------ctoping a tilted card of an image and making it straight------------------------

# img=cv2.imread("414.png")
# width=400
# height=450
# pts1=np.float32([[363,349],[580,337],[644,646],[396,664]])#all the  points of the card
# pts2=np.float32([[0,0],[width,0],[width,height],[0,height]])#the position of each point
# matrix=cv2.getPerspectiveTransform(pts1,pts2)#a matrix according to pts1 and pts2
# imgoutput=cv2.warpPerspective(img,matrix,(width,height))
#
# cv2.imshow("son",imgoutput)
#
# cv2.imshow("asld",img)
# cv2.imshow("adasdasd",img[300:700,364:650])
# cv2.waitKey(0)

#----------------------------add a grob of images in the same window--------------------------------------------
#method 1 # i think it need to be the same format (png,rbg,rgb)
# img=cv2.imread("414.png")
#
# imgs_horizontal=np.hstack((img,img))
# imgs_vertical=np.vstack((img,img))
#
# cv2.imshow("adasdasd",imgs_horizontal)
# cv2.waitKey(0)

#----------------------------detecting a color inside an image --------------------------------------------
# #0-convert img to HSV format
# #1-make a Trackbar for each attribute HSV(hue,saturation,brightness) not:in total 6 parameters (min and max)
# #2-find the best attributes for the color
# #3-marge with the original image to separate the wanted part/color
# def empt(a):
#     pass
#
# cv2.namedWindow("track")
# cv2.resizeWindow("track",600,400)
# cv2.createTrackbar("Hue min","track",0,179,empt)
# cv2.createTrackbar("Hue max","track",179,179,empt)
# cv2.createTrackbar("sat min","track",0,255,empt)
# cv2.createTrackbar("sat max","track",255,255,empt)
# cv2.createTrackbar("val min","track",0,255,empt)
# cv2.createTrackbar("val max","track",255,255,empt)
#
# while True:
#     img=cv2.imread("414.png")
#     imgH=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#convert to HSV
#     h_min = cv2.getTrackbarPos("Hue min","track")
#     h_max = cv2.getTrackbarPos("Hue max", "track")
#     s_min = cv2.getTrackbarPos("sat min", "track")
#     s_max = cv2.getTrackbarPos("sat max", "track")
#     v_min = cv2.getTrackbarPos("val min", "track")
#     v_max = cv2.getTrackbarPos("val max", "track")
#
#     print(h_min,h_max,s_min,s_max,v_min,v_max)
#     lower=np.array([h_min,s_min,v_min])
#     upper=np.array([h_max,s_max,v_max])
#     mask= cv2.inRange(imgH,lower,upper)
#
#     imgRes=cv2.bitwise_and(img,img,mask=mask)#marge
#
#
#     cv2.imshow("adasdasd0",img)
#     cv2.imshow("adasdasd1",imgH)
#     cv2.imshow("adasdasd2",mask)
#     cv2.imshow("adasdasd3", imgRes)
#     cv2.waitKey(1)
#----------------------------detecting a color inside an live feed--------------------------------------------
# def empt(a):
#     pass
# cv2.namedWindow("track")
# cv2.resizeWindow("track",600,400)
# cv2.createTrackbar("Hue min","track",0,179,empt)
# cv2.createTrackbar("Hue max","track",179,179,empt)
# cv2.createTrackbar("sat min","track",0,255,empt)
# cv2.createTrackbar("sat max","track",255,255,empt)
# cv2.createTrackbar("val min","track",0,255,empt)
# cv2.createTrackbar("val max","track",255,255,empt)
# cap=cv2.VideoCapture(0)
#
# while True:
#     while True:
#         succ,img=cap.read()
#         # findcolor(img,myColors)
#         imgH = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert to HSV
#         h_min = cv2.getTrackbarPos("Hue min", "track")
#         h_max = cv2.getTrackbarPos("Hue max", "track")
#         s_min = cv2.getTrackbarPos("sat min", "track")
#         s_max = cv2.getTrackbarPos("sat max", "track")
#         v_min = cv2.getTrackbarPos("val min", "track")
#         v_max = cv2.getTrackbarPos("val max", "track")
#
#         print(h_min, h_max, s_min, s_max, v_min, v_max)
#         lower = np.array([h_min, s_min, v_min])
#         upper = np.array([h_max, s_max, v_max])
#         mask = cv2.inRange(imgH, lower, upper)
#
#         imgRes = cv2.bitwise_and(img, img, mask=mask)  # marge
#
#         cv2.imshow("adasdasd0", img)
#         # cv2.imshow("adasdasd1", imgH)
#         # cv2.imshow("adasdasd2", mask)
#         cv2.imshow("adasdasd3", imgRes)
#         if cv2.waitKey(1) | 0XFF == ord('q'):
#             break
#----------------------------detecting a shape inside an image --------------------------------------------

# def getContours(img):#ملامح
#     #cv2.RETR_EXTERNAL : used to detect the 'outer' contours(corners and edges)
#     # APPROX method used to compress values we set it to non caz we dont need it compressed
#     contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#APPROX method used to compres valus we set it to non
#     for cnt in contours:
#         area=cv2.contourArea(cnt)
#         print(area)
#         if area>300:
#             cv2.drawContours(imgContour,cnt,-1,(255,0,0),0)
#             #calculating the curve length
#             peri=cv2.arcLength(cnt,True)#closed=True
#             # print(peri)#lenth of each contour arc
#             approx=cv2.approxPolyDP(cnt,0.02*peri,True)
#             print(len(approx))
#             objcon=len(approx)
#             x,y,w,h=cv2.boundingRect(approx)
#
#             if objcon==3:objtype="Tri"
#             elif objcon==4:objtype="sqour"
#             elif objcon==5:objtype="m5ms"
#             elif objcon>5 :objtype="cercle"
#
#             else:objtype="None"
#
#             cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
#             cv2.putText(imgContour,objtype,
#                         (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(0,0,255),1)
#
# img=cv2.imread("shapes.jpg")
# imgContour = img.copy()
# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to gray
# imgGrayBlur=cv2.GaussianBlur(imgGray,(7,7),1)# blur img
# imgGBC=cv2.Canny(imgGrayBlur,50,50)#detect edgs
# getContours(imgGBC)
#
# cv2.imshow("here",img)
# cv2.imshow("here2",imgGray)
# cv2.imshow("here3",imgGrayBlur)
# cv2.imshow("here4",imgGBC)
# cv2.imshow("here5",imgContour)
# cv2.waitKey(0)

#----------------------------face detection for a single photo (using default cascades)--------------------------------------------
# faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img= cv2.imread("download.jpg")
# imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces=faceCascade.detectMultiScale(imgGray,1.1,4)
# for (x,y,w,h) in faces:
#     cv2.rectangle(imgGray,(x,y),(x+w,y+h),(255,0,0),2)
#
# cv2.imshow("asd",imgGray)
# cv2.waitKey(0)

#----------------------------face detection for an live feed (using default cascades)--------------------------------------------

# faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # img= cv2.imread("download.jpg")
# cap=cv2.VideoCapture(0)
#
# while True:
#     succ,imgGray=cap.read()
#     # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(imgGray, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#     cv2.imshow("Video",imgGray)
#     if cv2.waitKey(1) | 0XFF == ord('q'):
#         break
# -------------------------------------------------------------------------------------------------------------
#-------------------------------------------project 1----------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# frameWidth=640
# frameHight=480
# cap=cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHight)
# cap.set(10,150)
#
# myColors=[[141,76,151,162,117,211],#my purbul
#           [5,107,0,19,255,255],#orange
#           [133,56,0,159,156,255],#purple
#           [57,76,0,100,255,255]]#green
# myColorsValues =[[78,66,223],#BGR
#                  [51,153,255],
#                  [255,0,255],
#                  [48, 153, 41]]
#
# myPoints=[] ##[x,y,  colorid]
# #141 162 76 117 151 211
# def findcolor(img,myColors,myColorsValues):
#     imgHVC=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     count=0
#     newPoints=[]
#     for color in myColors:
#         lower=np.array([color[0:3]])
#         upper=np.array([color[3:6]])
#         mask= cv2.inRange(imgHVC,lower,upper)
#         x,y=getContours(mask)
#         cv2.circle(imgResult,(x,y),10,myColorsValues[count],cv2.FILLED)
#         # if x!=0 and y!=0:
#         newPoints.append([x,y,count])
#         count+=1
#         # cv2.imshow(str(color[0]),mask)
#     return newPoints
# def getContours(img):#ملامح
#     #cv2.RETR_EXTERNAL : used to detect the 'outer' contours(corners and edges)
#     # APPROX method used to compress values we set it to non caz we dont need it compressed
#     contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#APPROX method used to compres valus we set it to non
#     x,y,w,h=0,0,0,0
#     for cnt in contours:
#         area=cv2.contourArea(cnt)
#         if area>1100:
#             cv2.drawContours(imgResult,cnt,-1,(255,0,0),1)
#
#             peri=cv2.arcLength(cnt,True)#closed=True
#
#             approx=cv2.approxPolyDP(cnt,0.02*peri,True)
#
#             x,y,w,h=cv2.boundingRect(approx)
#     return x+w//2,y
# def drawonCanvas(myPoints,myColorsValues):
#     for point in myPoints:
#         cv2.circle(imgResult, (point[0], point[1]), 10, myColorsValues[point[2]], cv2.FILLED)
#
# while True:
#     succ,img=cap.read()
#     imgResult=img.copy()
#     newPoints=findcolor(img,myColors,myColorsValues)
#     if len(newPoints)!=0:
#         for newP in newPoints:
#             myPoints.append(newP)
#     if len(newPoints) != 0:
#         drawonCanvas(myPoints,myColorsValues)
#     cv2.imshow("Video",imgResult)
#     if cv2.waitKey(1) | 0XFF == ord('q'):
#         break
# -------------------------------------------------------------------------------------------------------------
#-------------------------------------------project 2----------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#document detection

# Widthimg=480
# Heightimg=640
# cap=cv2.VideoCapture(0)
# cap.set(3,Widthimg)
# cap.set(5,Heightimg)
# cap.set(10,150)
#
# def preProcessing(img):
#     imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     imgGrayBlur=cv2.GaussianBlur(imgGray,(5,5),1)
#     imgCanny=cv2.Canny(imgGrayBlur,100,100)
#     kernil=np.ones((5,5))
#     imgDial=cv2.dilate(imgCanny,kernil,iterations=2)
#     imgThres=cv2.erode(imgDial,kernil,iterations=1)
#
#     return imgThres
# def getContours(img):#ملامح
#     maxArea=0
#     biggest=np.array([])
#     contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#APPROX method used to compres valus we set it to non
#     for cnt in contours:
#         area=cv2.contourArea(cnt)
#         if area>5000:
#             # cv2.drawContours(imgContour,cnt,-1,(255,0,0),0)
#
#             peri=cv2.arcLength(cnt,True)#closed=True
#             approx=cv2.approxPolyDP(cnt,0.02*peri,True)
#             if len(approx)==4 and area>maxArea:
#                 biggest=approx
#                 maxArea=area
#     cv2.drawContours(imgContour,biggest,-1,(255,0,0),20)
#     return biggest
# def reorder(myPoints):
#     myPoints=myPoints.reshape((4,2))
#     myPointsnew=np.zeros((4,1,2),np.int32)
#     add=myPoints.sum(1)
#
#
#     myPointsnew[0]=myPoints[np.argmin(add)]
#     myPointsnew[3]=myPoints[np.argmin(add)]
#     diff=np.diff(myPoints,axis=1)
#     myPointsnew[1]=myPoints[np.argmin(diff)]
#     myPointsnew[2]=myPoints[np.argmin(diff)]
#     return myPointsnew
#
#
#
# def getWarpp(img, biggest):
#     reorder(biggest)
#     pts1=np.float32(biggest)
#     pts2=np.float32([[0,0],[Widthimg,0],[Widthimg,Heightimg],[0,Heightimg]])
#     matrix=cv2.getPerspectiveTransform(pts1,pts2)
#     imgOutput=cv2.warpPerspective(img,matrix,(Widthimg,Heightimg))
#
#     return imgOutput
#
# while True:
#     suss,img=cap.read()
#     img = cv2.resize(img,(Widthimg,Heightimg))
#     imgContour=img.copy()
#
#     imgThres=preProcessing(img)
#     biggest=getContours(imgThres)
#     if len(biggest)==4:
#         imgwarpped=getWarpp(img,biggest)
#         cv2.imshow("Vide3o", imgwarpped)
#
#     cv2.imshow("Video",     imgContour)
#     cv2.imshow("Vide2o",     img)
#     if cv2.waitKey(1) | 0XFF == ord('q'):
#         break
# -------------------------------------------------------------------------------------------------------------
#-------------------------------------------project 3----------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------




