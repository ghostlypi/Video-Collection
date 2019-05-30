import numpy as np
import cv2
import Greyify as g

cap = cv2.VideoCapture(0)

count = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    if count % 10 == 0:
        cv2.imwrite("C:\\users\\parth\\Human Pictures\\Data\\Unsorted\\frame%d.jpg" % count, frame)
    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
