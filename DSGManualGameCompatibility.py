from sympy import true

from Menu import Menu
import logging
from DSGFileHandler import InputHandler, OutputHandler, Utility
from difflib import SequenceMatcher

from Models import Player

logger=logging.getLogger(__name__)

def similar_strings(to_compare:str, to_match:str) -> float:
    """Takes in two strings and returns a float of the percentage they are similar to each other

    Parameters
    ----------
    to_compare : str
        The string you want to compare
    to_match : str
        The string you want to compare against

    Returns
    -------
    float
        The ratio of the similarity between to strings
    """
    # Remove excess whitespace
    to_compare = to_compare.strip()
    to_match = to_match.strip()
    return SequenceMatcher(None, to_compare, to_match).ratio()

def suggest_word(input_word:str, word_list:list[str]) -> tuple[str,float]:
    """Takes in a string and a list of words and returns the most likely word

    Parameters
    ----------
    input_word : str
        The word you want to check for similarity

    word_list : list[str]
        The list of words to test input_word against for similarity

    Returns
    -------
    str
        The most similar word, can also be empty string if none had more than %10 similarity
    """
    similarities = {}
    for current_word in word_list:
        similarities[current_word] = similar_strings(input_word, current_word)
    similarities = dict(sorted(similarities.items(),key=lambda x:x[1], reverse=true))
    for word in similarities:
        return (word,similarities[word])     # Return first word in dictionary
    return ("",0)

def getPlayerInput(PlayersDict=InputHandler.ParseDSGYaml(), PlayerID:str="Player") -> Player | None:
    Player=input(f"Name Of {PlayerID}:")
    PlayerObj=PlayersDict.get(Player)
    if not PlayerObj:
        print("There is No Player by That Name")
        SimilarWordTuple=suggest_word(Player,list(PlayersDict))
        if SimilarWordTuple[1]> 0.01:
            print(f'Did you mean "{SimilarWordTuple[0]}" ({SimilarWordTuple[1]:.0%}  Sure)')
    else:
        return PlayerObj

def ListPlayerCompatibles(Player1:str="",Player2:str=""):
    PlayersDict=InputHandler.ParseDSGYaml()
    try:
        while(True):
            if not Player1:
                PlayerObj1=getPlayerInput(PlayersDict,"Player 1")
            else:
                PlayerObj1=PlayersDict.get(Player1)
                Player1=""
            if PlayerObj1:
                break
            else:
                continue
        while(True):
            if not Player2:
                PlayerObj2=getPlayerInput(PlayersDict,"Player 2")
            else:
                PlayerObj2=PlayersDict.get(Player2)
                Player2=""
            if PlayerObj2:
                break
            else:
                continue
        print(f'{PlayerObj1}: {PlayerObj2} {PlayerObj2.acceptable_worlds & PlayerObj1.acceptable_worlds}')
    except KeyboardInterrupt:
        pass

def ListPlayerGames(PlayerName:str=""):
    
    PlayersDict=InputHandler.ParseDSGYaml()
    try:
        while(True):
            if not PlayerName:
                PlayerObj=getPlayerInput(PlayersDict)
            else:
                PlayerObj=PlayersDict.get(PlayerName)
                PlayerName=""
            if PlayerObj:
                PlayerObj.printWorlds()
                break
            else:
                continue
    except KeyboardInterrupt:
        pass


def ListAllPlayers():
    PlayersDict=InputHandler.ParseDSGYaml()
    for index, key in enumerate(PlayersDict):
        print(index, key)
    pass

def Main():
    print(f"Functionality Not Integrated Yet")
    logger.error(f"Functionality Not Integrated Yet")
    listOfActions=[
        ('List all Players', ListAllPlayers),
        ("List Player's Games", ListPlayerGames),
        ("List 2 Player's Compatibility", ListPlayerCompatibles),
    ]
    Menu.menu('\nManual Player Game Compatibility',listOfActions)
    pass


if __name__ == "__main__":
    Utility.MakeDir("logs")
    logging.basicConfig(filename='logs/ManualCompare.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    Main()