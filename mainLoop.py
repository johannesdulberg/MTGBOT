from basicFunctionality import *
from advancedFunctionality import *
from cardDetection import *
from getHand import *
from variables import *

def gameMainLoop():
    """
    Main Loop
    () -> bool result
    bool result  #True if Win False i Loss

    Other Variables:
    int land #Keeps Track of played Lands
    int mana #Keeps track of mana thats usable
    list handWithPos #List of tuples with card as string on the first index and position on the second
    bool landplay #landplay keeps track of wether a land is played this turn True is land played this turn
    bool main #if the first mainphase was used to play cards main will be set to true. Its for fixing a bug where the bot skips phases
    """
    result=False

    print("MATCH STARTED")

    while not gameOver():
        main=False
        time.sleep(0.1)
        if skipPhaseButtonIsSkippable() or doubleBlock():
            if isMain(): 
                print("ITS FIRST MAIN PHASE")
            
                main=True
                landplay=False
                print("GET HAND")
                hand=getHand(False,0) #0 for first mainphase
                print("Hand: ",hand)
                

                playSheet(hand,0) #0 for first mainphase
                print("HAND AFTER PLAY: ",hand)

            if isSecondMain():
                print("ITS SECOND MAIN PHASE")
                print("LANDS: ",lands,"MANA",mana)

                if not main:
                    landplay=False

                hand=getHand(False,1) #1 for first mainphase
                playSheet(hand,1) #1 for first mainphase

            if not isMain() or doubleBlock():
                if not gameOver():
                    pa.click(800,150) #clicks at opponent for attacking him insted of planeswalker
                    pa.click(800,800)  #clicks on our player for resolving different spells
                    print("SKIPPING TO NEXT PHASE")              
                    pa.keyDown("space")
                    pa.keyUp("space")    



    #todo
    return result