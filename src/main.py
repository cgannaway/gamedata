import numpy as np
import time
import capture
import cv2

#monitor 1 health location r6:s - 1920x1080
r6monitor1 = np.array([670,965,735,1000])

#monitor1 health location csgo - 1920x1080
csmonitor1 = np.array([50,1030,120,1070])

def mainLoop():
    last_time = time.time()
    while True:
        img = screencapture.screen_record()
        num = recognition.imgtostring(img)
        
        print('loop took {} seconds. health: '.format(time.time()-last_time) + num )
        last_time = time.time()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    screencapture = capture.screenCap(csmonitor1[0], csmonitor1[1], csmonitor1[2], csmonitor1[3])
    recognition = capture.ocr()
    mainLoop()