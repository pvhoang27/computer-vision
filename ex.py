import cv2 

image = cv2.imread("001771721_jpg.rf.687025a63ae5c9e58f2454ab1e41eaa9.jpg")
height ,width , _ = image.shape

with open("001771721_jpg.rf.687025a63ae5c9e58f2454ab1e41eaa9.txt" , "r") as to :
  annotation = to.readlines()
annotation = [anno.rstrip().split(" ") for anno  in  annotation]
for  anno in annotation: 
  category, x , y , w , h = anno 
  xcent= float(x) * width
  ycent = float(y) * height
  w = float(w)* width
  h = float(h)* height
  xtl = int(xcent - w /2 )
  ytl = int(ycent - h / 2)
  xbr = int(xcent + w / 2) 
  ybr = int(ycent + h / 2)
  cv2.rectangle(image, (xtl, ytl), (xbr , ybr), (0, 255, 0), 2)

cv2.imwrite("sample.jpg", image)

