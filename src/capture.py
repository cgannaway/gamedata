import numpy as np
from PIL import ImageGrab, Image
import cv2
import time

class screenCap:

    def __init__(self, lx, ty, rx, by):
        self.lx = lx
        self.ty = ty
        self.rx = rx
        self.by = by

    def screen_record(self):
        # bounding box is left x, top y, right x, bottom y
        capture = ImageGrab.grab(bbox=(self.lx, self.ty, self.rx, self.by))
        printscreen =  np.array(capture)
        
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
        return printscreen
            


