
"""GLOBAL VARIABLES"""

lands=0
mana=0
landplay=False



"""CARD SLURS""" 
"""Must have matching .png image in assets"""

"""CARDS IN DECK OF LEONIDAS"""
cards=["falkenrath","light","land","grim","calv","chandra","goblin","py","redfell","shock","spitter","tin","inst","rapt"]

"""CARDS IN DECK OF XERXIS"""
#cards=["falkenrath","light","land","grim","calv","chandra","goblin","py","redfell","shock","spitter","tin"]


"""MANA DICTIONARY"""
"""matches Card names with their converted mana cost"""
manaDict={"land":0 ,"grim":1,"calv":2,"chandra":3,"goblin":3,"light":1,"py":2,"redfell":4,"shock":1,"spitter":1,"tin":1,"rapt":2,"inst":2}


"""CARD X POSITIONS IN HAND"""
landplay=False
Positions1=[800]
Positions2=[712,870]
Positions3=[650,800,950]
Positions4=[590,730,860,1000]
Positions5=[500,650,800,950,1100]
Positions6=[460,590,730,860,1000,1140]
Positions7=[350,500,650,800,950,1100,1250]
Positions8=[330,460,590,730,860,1000,1140,1280]

"""REVERSE THE POSITIONS IN HAND"""
def rev():
    Positions1.reverse()
    Positions2.reverse()
    Positions3.reverse()
    Positions4.reverse()
    Positions5.reverse()
    Positions6.reverse()
    Positions7.reverse()
    Positions8.reverse()



"""PLAY SHEET FOR XERXIS"""

"""FRIST MAIN PHASE"""
"""
land1Plays=["grim","spitter","tin"]
land2Plays=["calv","py","grim","grim","spitter","spitter","tin","tin","shock","shock"]
land3Plays=["chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock"]
land4Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land5Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land6Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land7Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land8Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land9Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land10Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land11Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
"""

"""SECOND MAIN PHASE"""
"""
land1Plays2=["grim","spitter","tin"]
land2Plays2=["light","calv","py","grim","grim","spitter","spitter","tin","tin","shock","shock"]
land3Plays2=["light","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock"]
land4Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land5Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land6Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land7Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land8Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land9Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land10Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
land11Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","shock","shock","light"]
"""


"""PLAYSHEET FOR LEONIDAS"""

"""FRIST MAIN PHASE"""
land1Plays=["grim","spitter","tin"]
land2Plays=["calv","py","grim","grim","spitter","spitter","inst","rapt","tin","tin","shock","shock"]
land3Plays=["chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock"]
land4Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land5Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land6Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land7Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land8Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land9Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land10Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land11Plays=["redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]

"""SECOND MAIN PHASE"""
land1Plays2=["grim","spitter","tin"]
land2Plays2=["light","calv","py","grim","grim","spitter","spitter","inst","rapt","tin","tin","shock","shock"]
land3Plays2=["light","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock"]
land4Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land5Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","light"]
land6Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land7Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land8Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land9Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land10Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]
land11Plays2=["light","redfell","chandra","calv","goblin","grim","grim","spitter","spitter","tin","tin","py","inst","rapt","shock","shock","light"]

