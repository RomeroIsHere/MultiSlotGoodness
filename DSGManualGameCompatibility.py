from itertools import cycle

from Menu import Menu
import logging
from DSGFileHandler import InputHandler, OutputHandler, Utility


from Models import Player

logger=logging.getLogger(__name__)

def ListCycle():
    CycleDict=InputHandler.ParseCycleYamls()
    
    AllSlots=list(CycleDict)
    AlreadyVisitedSet: set[str]=set()
    StartingSlot=CurrSlot=AllSlots[0]
    PlayerInfoDict=CycleDict.get(StartingSlot)
    NextSlot=''
    if isinstance(PlayerInfoDict,dict):
        NextSlot=PlayerInfoDict.get('SendTo')
    
    while not (StartingSlot == NextSlot):
        PlayerInfoDict=CycleDict.get(CurrSlot)
        if isinstance(PlayerInfoDict,dict):
            NextSlot=PlayerInfoDict.get('SendTo')
        print(f"{CurrSlot} -> {NextSlot}")
        CurrSlot=NextSlot
        pass
    pass

def getPlayerInput(PlayersDict, PlayerID:str="Player") -> Player | None:
    if not PlayersDict:
        PlayersDict= InputHandler.ParseDSGYaml()
    Player=input(f"Name Of {PlayerID}:")
    PlayerObj=PlayersDict.get(Player)
    if not PlayerObj:
        print("There is No Player by That Name")
        SimilarWordTuple=Utility.suggest_word(Player,list(PlayersDict))
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
        ("List Cycle from File", ListCycle),
    ]
    Menu.menu('\nManual Player Game Compatibility',listOfActions)
    pass


if __name__ == "__main__":
    Utility.MakeDir("logs")
    logging.basicConfig(filename='logs/ManualCompare.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    Main()