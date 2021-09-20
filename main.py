
from mainLoop import *
from variables import *
from cardDetection import *

def get15Wins(): #todo
    """
    Plays the Game until it hits 15 Wins
    ()-> None
    """

    for i in range(50):
        print("MATCH: ",i)
        newGame() 
        gameMainLoop()

def playXGames(x):
    """
    Plays X Matches
    (int x) -> None
    int x #Number of Matches to Play
    """
    for i in range(x):
        print("MATCH: ",i)
        newGame() 
        gameMainLoop()

def playThisGame():
    """
    Plays This Match thats alreay Started
    () -> None
    """
    gameMainLoop()

def playOneGame():
    """
    Plays One Match
    () -> None
    """
    newGame() 
    gameMainLoop()

playThisGame()