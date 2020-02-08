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
        color =  np.array(capture)
        bw = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
        cv2.imshow('window',bw)
        
        return bw
            


