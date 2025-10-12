import cv2 

image = cv2.imread("001771721_jpg.rf.687025a63ae5c9e58f2454ab1e41eaa9.jpg")

height ,width , _ = image.shape

with open("001771721_jpg.rf.687025a63ae5c9e58f2454ab1e41eaa9.txt" , "r") as to :
  annotation = to.readlines()

# print(annotation)

annotation = [anno.rstrip().split(" ") for anno  in  annotation]

# print(annotation)
for  anno in annotation: 
  category, x , y , w , h = anno 
  x = float(x)
  y = float(y)
  w = float(w)
  h = float(h)
  cv2.rectangle(image, (5, 5), (220, 220), (255, 0, 0), 2)

