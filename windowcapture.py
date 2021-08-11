## https://www.youtube.com/watch?v=WymCpVUPWQ4&ab_channel=LearnCodeByGaming
# Ik was bij bovenstaande video gebleven. Hij gebruikt iets van Windows; ik gebruik mss voor screenshots.
# MINUUT: 16:00 gaat hij uitleggen hoe we nog verder kunnen optimaliseren.

import cv2 as cv
import numpy as np
import os
import pyautogui
import time
from PIL import ImageGrab
import mss


class WindowCapture():
    
    def get_screenshot(self):   
        # define the monitor width and height
        w = 800
        h = 640

        monitor = {"top": 0, "left": 0, "width": w, "height": h}
        title = 'RS Bot'
        sct = mss.mss()
        img = np.asarray(sct.grab(monitor))

        #Drop the alpha channel on the image (transparanty) - drops perforance (50%)
        img = img[...,:3]
        img = np.ascontiguousarray(img)
        return img


    while "Screen capturing":
        last_time = time.time()
        # Get raw pixels from the screen, save it to a Numpy array
        screenshot = window_capture()

        # Display the picture
        cv.imshow("OpenCV/Numpy normal", screenshot)
            
        print("fps: {}".format(1 / (time.time() - last_time)))
        # Press "q" to quit
        if cv.waitKey(25) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break