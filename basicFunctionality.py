import pyautogui as pa
import time
from variables import *

def isMain():
    """
    Checks if its first mainphase
    () -> bool
    """

    if pa.pixel(698,791)[0]>200 and not pa.pixel(800,800)[0]>230:
        return True           
    else:
        return False

def isSecondMain():
    """
    Checks if its second mainphase
    () -> bool
    """
    if pa.pixel(904,791)[0]>200 and not pa.pixel(800,800)[0]>230:
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
    
    victory= pa.pixel(610,480)[0]>230 and pa.pixel(610,480)[1]>230 and pa.pixel(610,480)[2]>230 and pa.pixel(942,553)[0]>230 and pa.pixel(942,553)[1]>230 and pa.pixel(942,553)[2]>230
    loss=pa.pixel(673,538)[0]>230 and pa.pixel(673,538)[1]>230 and pa.pixel(673,538)[2]>230 and pa.pixel(925,495)[0]>230 and pa.pixel(925,495)[1]>230 and pa.pixel(925,495)[2]>230
    if victory or loss:
        print("GG")
        time.sleep(0.3)

        if victory:
            print("VICTORY")
            rev()
            return True

        if loss:
            print("GAME OVER")
            rev()
            return True

        else:
            return False

    else:   
        return False
        
def skipPhaseButtonIsSkippable():
    """
    checks if the skip to next Phase/resolve button is clickable
    () -> bool
    """
    if (pa.pixel(1556,849)[0]>230 and pa.pixel(1556,849)[2]<100) or (pa.pixel(1556,849)[0]<150 and pa.pixel(1556,849)[2]>240):
        return True
    else:
        return False

def doubleBlock():
    if pa.pixel(800,800)[0]>230:
        return True
    else:
        return False