import pyautogui as pa
import time
from variables import *

def isMain():
    """
    Checks if its first mainphase
    () -> bool
    """
    if pa.pixel(698,791)[0]>200:
        return True           
    else:
        return False

def isSecondMain():
    """
    Checks if its second mainphase
    () -> bool
    """
    if pa.pixel(904,791)[0]>200:
        return True           
    else:
        return False


def newGame():
    """
    Starts a new game from home menu and accepts the Hand without mulligan
    () -> None
    """

    print("NEW GAME")
    while 1:
            pa.click(50,500)
            time.sleep(1)
            if pa.pixel(1422,903)[0]>180: #play Button
                pa.mouseDown(1422,903,button="left")
                pa.mouseUp(1422,903,button="left")
            if pa.pixel(956,795)[0]>180: #mulligan Button
                break

    while True:
        time.sleep(1)
        if pa.pixel(956,795)[0]>180: #mulligan Button
            pa.mouseDown(934,784,button="left")
            pa.mouseUp(934,784,button="left")
            break

def gameOver():
    """
    Checks if the game is over
    ()-> bool
    
    """
    gameOverCounter=0
    if pa.pixel(1441 ,897)[0]>230 and pa.pixel(1441 ,897)[1]>230 and pa.pixel(1441 ,897)[2]>230 and pa.pixel(1312,87)[2]>200 and pa.pixel(1312,87)[0]<140:

        gameOverCounter+=1
        if gameOverCounter>2:
            print("GAME OVER")
            rev()
            return False
        else:
            return True
    else:   
        gameOverCounter=0
        return True
        
