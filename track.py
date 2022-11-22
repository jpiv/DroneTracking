import cv2
import numpy as np
from PIL import Image
import math
import imutils


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
  ret, frame = cam.read()
  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  ret, filtered_frame = cv2.threshold(gray_frame, 55, 255, cv2.THRESH_BINARY)

  template = cv2.imread('./temp.png', 0)
  w, h = template.shape[::-1]
  for scale in np.linspace(0.05, 1.0, 10)[::-1]:
    # according to scale Scale the image , And maintain its aspect ratio 
    resized_frame = imutils.resize(template, width=int(template.shape[1] * scale))
  # Edge detection in the scaled grayscale image , Template matching 
  # The image is calculated using exactly the same parameters as the template image Canny Edge representation ;
  # Use cv2.matchTemplate Apply template matching ;
  # cv2.minMaxLoc Get the relevant results and return a 4 Tuples , Which contains the minimum correlation value 、 Maximum correlation value 、 The minimum （x,y） Coordinates and maximum values （x,y） coordinate . We only deal with the maximum and （x,y）- Coordinates of interest , Therefore, only the maximum value is retained and the minimum value is discarded .
    # edged = cv2.Canny(resized_frame, 50, 200)
    # filtered_frame = resized_frame
    res = cv2.matchTemplate(filtered_frame,resized_frame,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    zipped_locs = [l for l in zip(*loc[::-1])]
    pt = zipped_locs[0] if len(zipped_locs) else None
    # for pt in zipped_locs:
    if pt:
      cv2.rectangle(frame, pt, (math.floor(pt[0] + w * scale), math.floor(pt[1] + h * scale)), (0,0,255), 1)




  if not ret:
      print("failed to grab frame")
      break

  cv2.imshow("test",  frame)

  k = cv2.waitKey(1)
  if k%256 == 27:
      # ESC pressed
      print("Escape hit, closing...")
      break

cam.release()

cv2.destroyAllWindows()