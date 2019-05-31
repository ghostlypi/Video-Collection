import numpy as np
import cv2
import Greyify as g
import time

cap = cv2.VideoCapture(0)

def capture(path, limit):
    count = int(np.random.random()*1000000)
    limit = limit*10 + count
    path += "\\"

    while(count < limit):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        if count % 10 == 0:
            cv2.imwrite( path+"frame%d.jpg" % count, frame)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


