from variables import *
from cardDetection import *
from advancedFunctionality import *
import pyautogui as pa


def countCardsBool(pos):
    """
    Checks if there is a Card at the given x Position 
    (int x) -> bool
    """

    pa.moveTo(pos,940,0.2)
    if pa.pixel(pos-20,940)[0]+pa.pixel(pos-20,940)[1]+pa.pixel(pos-20,940)[2]<120 and pa.pixel(pos,920)[0]+pa.pixel(pos,920)[1]+pa.pixel(pos,920)[2]>450:
        return True
    else:
        return False
    


def countCards():
    """
    Counts the cards held in hand
    () -> int 
    """

    handCardOuterBoundries=[1355,1300,1230,1150,1090,1015,944,870]

    for i in range(8):

        if countCardsBool(handCardOuterBoundries[i]):
            print("THERE ARE ",8-i," CARDS IN HAND")
            return 8-i

    return 0



def getHand(landPlayedInThisGetHand,turn):
    """
    Get the names of all Cards held in hand and returns a List of Tuples with the name of the Card at the first and the position of the card at the second position
    (bool landPlayedInThisGetHand,int turn) -> list 

    Variables
    bool landPlayedInThisGetHand #Is False when called from mainloop. Recursivly plays a land as soon as the cursor hovers over a Land. Then calls it self again to return the Hand to the mainloop

    """


    global landplay
    hands={}
    hand=[]
    cardCount=countCards()

    for i in range(cardCount):
        for card in cards:
            lookup=lookUp(goto(i,cardCount),card)
            if lookup == 2 and landPlayedInThisGetHand==False and landplay==False:
                landUp()
                return getHand(True,0)

            if lookup:
                hands[i]=card
                break
        
    for i in range(cardCount):
        if i in hands:
            hand.append(hands[i])

        else:
            hand.append("NONE")

    handWithPosTemp=[]
    if cardCount>0:
        for (x, y) in zip(hand, eval(f"Positions{cardCount}")):
            handWithPosTemp.append((x,y))

    return handWithPosTemp

