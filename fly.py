import sys
from PIL import Image
import cv2
sys.path.insert(0, './Tello-Python/Tello_Video')
from tello import Tello

t = Tello('', 9000)

cv2.namedWindow("test")

while True:
  frame = t.read()
  if frame is not None and len(frame) > 0:
    print(frame)
    # image = Image.fromarray(frame)
    cv2.imshow("test",frame)
    k = cv2.waitKey(1)
