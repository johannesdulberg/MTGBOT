import pyautogui as pa
import time
from variables import *
from basicFunctionality import *

def goto(num,cardCount):
    """
    Moves the Cursor to the position of a Card
    (int num, cardCount)-> int x
    int num #The number of the card to go to
    int cardCount #number of cards in hand
    int x #position of the card and the curser after the move
    """

    y=937
    x=eval(f"Positions{cardCount}")[num]
    pa.moveTo(x,y,0.01)
    
    return x

def landUp():
    """
    Playes a Land and changes lands and mana +1
    ()->None
    """

    global lands
    global mana
    global landplay

    lands+=1
    if lands==2:
        rev()
    mana+=1
    landplay=True
    pa.click(clicks=2, interval=0.25)
    

        
def playSheet(hand,phase):
    """
    This Function is responible for playing the recommended cards
    (list hand, int turn) -> None
    """

    global lands
    global mana

    if phase==0:
        for i in eval(f"land{lands}Plays"):
            hand=playCard(hand,i)
            time.sleep(0.1)
            if not isMain:
                break

        if isMain():    
            pa.keyDown("space")
            pa.keyUp("space")

    if phase == 1:
        for i in eval(f"land{lands}Plays2"):              
            hand=playCard(hand,i)
            time.sleep(0.05)
            if not isSecondMain:
                break

        if isSecondMain():
            pa.keyDown("space")
            pa.keyUp("space")


def playCard(hand,card):
    """
    This Function is responible for actually playing cards except of Lands
    (list hand, String card) -> list hand
    """

    global lands
    global mana
    yPlay=937

    
    pos=getPositon(hand,card)
    if pos and mana-manaDict[card]>=0:
        print("PLAYING: ",card)
        mana=mana-manaDict[card]
        pa.moveTo(pos,yPlay,0.2)
        pa.click(pos,yPlay,2,0.2,button="left")
        pa.click(10,500) #Somewhere
        time.sleep(0.3)
        pa.click(809,157) #Opponent
        time.sleep(4) #Wait for opponent to resolve todo
        pa.click(1000,460,clicks=2, interval=0.1) #for double Cards like light up the stage
        pa.click(600,460,clicks=2, interval=0.03)
        pa.keyDown("z") #fallback if card isnt playable
        pa.keyUp("z")

        """removes the played card and saves a new hand with new positions"""
        hand=list(map(lambda x: x[0],hand))
        hand.remove(card)
        handWithPosTemp=[]
        if len(hand)>0:
            for (x, y) in zip(hand, eval(f"Positions{len(hand)}")):
                handWithPosTemp.append((x,y))

        hand=handWithPosTemp

    return hand
    

def getPositon(hand,card):
    """
    Gets the  x position of a card in a hand
    (list hand, String card) -> int x or boolean
    """

    handWithoutPositions=list(map(lambda x: x[0],hand))
    if card in handWithoutPositions:
        cardIndex=handWithoutPositions.index(card)
        return hand[cardIndex][1]

    else:
        return False