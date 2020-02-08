import numpy as np
import time
import capture
import ocr
import cv2

#monitor 1 health location
monitor1 = np.array([670,965,735,1000])
#monitor 2 health location. is black for some reason
monitor2 = np.array([2590,965,2655,1000])

def mainLoop():
    last_time = time.time()
    while True:
        img = screencapture.screen_record()
        num = recognition.toNumber(img)
        
        print('loop took {} seconds. health: '.format(time.time()-last_time) + num )
        last_time = time.time()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    screencapture = capture.screenCap(monitor1[0], monitor1[1], monitor1[2], monitor1[3])
    recognition = ocr.ocr()
    mainLoop()