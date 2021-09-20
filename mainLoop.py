from basicFunctionality import *
from advancedFunctionality import *
from cardDetection import *
from getHand import *
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

    global lands
    global mana
    global handWithPos
    global landplay
    result=False

    print("MATCH STARTED")

    while gameOver():
        main=False
        time.sleep(7)
        
        if isMain(): 
            print("ITS FIRST MAIN PHASE")
            main=True
            landplay=False
            print("GET HAND")
            hand=getHand(False,0) #0 for first mainphase
            print("Hand: ")
            print("GOTO PLAYSHEET")
            playSheet(hand,0) #0 for first mainphase

        if isSecondMain():
            print("ITS SECOND MAIN PHASE")

            if not main:
                landplay=False

            hand=getHand(False,1) #1 for first mainphase
            playSheet(hand,1) #1 for first mainphase

        if not isMain():
                pa.click(800,150) #clicks at opponent for attacking him insted of planeswalker
                time.sleep(0.1)
                pa.click(800,800)  #clicks on our player for resolving different spells
                print("SKIPPING TO NEXT PHASE")              
                pa.keyDown("space")
                pa.keyUp("space")    



    #todo
    return result