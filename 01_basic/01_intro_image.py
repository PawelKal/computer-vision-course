import cv2

print(cv2.__version__)

image = cv2.imread(filename = "/home/pawel/PycharmProjects/computer-vision-course/01_basic/assets/bear.jpg")

cv2.imshow(winname='image', mat=image)

cv2.waitKey(delay=5000)