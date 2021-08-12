## IK WAS BIJ MINUUT 7 VAN: 
# https://www.youtube.com/watch?v=7k4j-uL8WSQ&list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI&index=5

import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import findClickPositions

# initialize the WindowCapture class
wincap = WindowCapture('Runescape')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    #cv.imshow('Computer Vision', screenshot)
    findClickPositions(needleImage, screenshot, threshold=0.5)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')