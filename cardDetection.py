
from variables import *
from os import error
import d3dshot
import time
import cv2
import numpy as np
import pyautogui as pa
import os


def lookUp(x,card):
    """
    Card detection with openCV takes x-Position and a card to look for. Takes a screenshot based on the x Position to template match. 
    Takes a Position and a Card to Match. Returns True if card was Matched and 2 if its the first land per turn. 
    (int x, String card) -> bool or int 2
    
    
    
    """

    global landplay
    
    xl=x-200
    xr=x+200
    yo=650
    yu=790
    d = d3dshot.create()
    d.screenshot_to_disk(region=(xl,yo,xr,yu),file_name="shot.png",directory=r"C:\Users\Johannes\MTG_BOT\MTG_BOT_V2\assets")
    hay = cv2.imread(r"C:\Users\Johannes\MTG_BOT\MTG_BOT_V2\assets\shot.png")
    needle = cv2.imread(os.path.join(r"C:\Users\Johannes\MTG_BOT\MTG_BOT_V2\assets", f"{card}.png"))

    """
    #SHOW IMAGE
    cv2.imshow('Needle', hay)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imshow('Needle', needle)
    cv2.waitKey()
    cv2.destroyAllWindows()  
    """

    result = cv2.matchTemplate(hay, needle, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    w = needle.shape[1]
    h = needle.shape[0]
    cv2.rectangle(hay, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
    threshold = .55
    yloc, xloc = np.where(result >= threshold)
    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    if len(rectangles)==0:
        return False

    if len(rectangles)==1 and card=="land" and landplay==False:
        print("PLAYING A LAND")
        return 2

    if len(rectangles)==1:
        return True
        
    else:
        return False





