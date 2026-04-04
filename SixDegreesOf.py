import logging
from Models import Player
from DSGFileHandler import YamlFilesHandling
from typing import Any

logger=logging.getLogger(__name__)

def RecursiveDegree(PlayerDict:dict[str,Player], NuList:set[Player], CurrentDegree=1):
    for playerObj in NuList:
        if not playerObj.HasBeenVisited:
            playerObj.HasBeenVisited=True
            if playerObj.DegreeOf < 0:
                playerObj.DegreeOf=CurrentDegree
            else:
                playerObj.DegreeOf=min(CurrentDegree,playerObj.DegreeOf)
    NewCompatibleList=set()
    for playerObj in NuList:
        for Sub in playerObj.CompatiblePlayers:
            if not PlayerDict[Sub].HasBeenVisited:
                NewCompatibleList.add(PlayerDict[Sub])
    
    if len(NewCompatibleList):
        RecursiveDegree(PlayerDict, NewCompatibleList, CurrentDegree+1)
    print(f" Finished Current Depth {CurrentDegree}")

def DegreesOf(PlayerDict:dict[str,Player], SlotName='Meli', CurrentDegree=1):
    PlayerDict[SlotName].HasBeenVisited=True
    PlayerDict[SlotName].DegreeOf=0
    for playerName in PlayerDict[SlotName].CompatiblePlayers:
        playerObj=PlayerDict[playerName]
        if not playerObj.HasBeenVisited:
            playerObj.HasBeenVisited=True
            if playerObj.DegreeOf < 0:
                playerObj.DegreeOf=CurrentDegree
            else:
                playerObj.DegreeOf=min(CurrentDegree,playerObj.DegreeOf)
    NewCompatibleList=set()
    for playerName in PlayerDict[SlotName].CompatiblePlayers:
        playerObj=PlayerDict[playerName]
        for Sub in playerObj.CompatiblePlayers:
            if not PlayerDict[Sub].HasBeenVisited:
                NewCompatibleList.add(PlayerDict[Sub])
    if len(NewCompatibleList):
        RecursiveDegree(PlayerDict, NewCompatibleList, CurrentDegree+1)
    else:
        print(f" Finished Current Depth {CurrentDegree} with name {SlotName}")

    pass

def ResetDegrees(PlayerDict:dict[str,Player]):
    for _, Player in PlayerDict.items():
        Player.HasBeenVisited=False
        Player.DegreeOf=-1

def LogMaxDegree(PlayerDict:dict[str,Player], MaxDegreeDict:dict[str,Any|int]):
    for name, PlayerObj in PlayerDict.items():
        MaxDegreeDict[name] = max(PlayerObj.DegreeOf,MaxDegreeDict.get(name,0))
    pass
if __name__ =="__main__":
    logging.basicConfig(filename='logs/DegreesOf.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    PlayerDict=YamlFilesHandling.ParseDSGYaml()
    

    DiameterDict=dict()
    for Name in PlayerDict:
        DegreesOf(PlayerDict,Name)
        LogMaxDegree(PlayerDict,DiameterDict)
        ResetDegrees(PlayerDict)
        pass
    for name, player in DiameterDict.items():
       
       print(f'{name}: {player}')