import logging
import yaml
import csv
import os
import time
from  Graph import Graph
from Players import Player

logger=logging.getLogger(__name__)

def ParseDSGYaml(shouldPrint=False) -> dict[str,Player]:
    DSGDataPath="DSG-data.yaml"
    logger.info(f"Parsing YAML {DSGDataPath}")
    with open(DSGDataPath) as stream:
        try:
            yamlObject=yaml.safe_load(stream)
            TempPlayerDict=dict() # [str,Player]
            PlayerSlotsName =yamlObject.get('SlotName')
            logger.info(f"Number Of Players:{len(PlayerSlotsName)}")
            # Add a Player with an ID to use as an index
            for id, Slot in enumerate(PlayerSlotsName):
                TempPlayerDict[Slot]=(Player(Slot, id))
            
            WorldList=yamlObject.get('Worlds')
            if not (WorldList):
                logger.warning(f"{DSGDataPath} Has no Worlds Registered")
            else:
                logger.info(f"Found {len(WorldList.keys())} worlds in {DSGDataPath}")
                for WorldName in WorldList.keys():
                    logger.debug(f"Handling World {WorldName}")
                    for Slot in WorldList[WorldName]:
                        # Check if Slot is One of the Players
                        if not (Slot in PlayerSlotsName):
                            if Slot:
                                logger.warning(f"Player not in List:{Slot}")
                            else:
                                logger.warning(f"Empty World:{WorldName}")
                        else:
                            #Since it is
                            logger.debug(f"\tPlayer {Slot} in World {WorldName}")
                            # Add it the World to the Player
                            TempPlayerDict[Slot].acceptable_worlds.add(WorldName)
                            
                            for Partner in WorldList[WorldName]:
                                # then add Every Compatible Player in List if their a Valid player
                                if (Partner in PlayerSlotsName):
                                    TempPlayerDict[Slot].AddToCompatible(TempPlayerDict[Partner])
                                else:
                                    logger.warning(f"Player {Partner} in World {WorldName} not in Playerlist")
            # Now Get the List of Exclusions
            ExcludeList=yamlObject.get('ExclusionList')
            if not ExcludeList:
                logger.info("No exclusions to take care of")
            else:
                logger.info("Handling Exclusions")
                for list in ExcludeList.keys():
                    logger.info(f"Handling Excluding List {list}")
                    for Slot in ExcludeList[list]:
                        logger.debug(f"Handling Player {Slot}")
                        for Partner in ExcludeList[list]:
                            logger.debug(f"Excluding Partner {Partner} From Player {Slot}")
                            if (Partner in PlayerSlotsName):
                                TempPlayerDict[Slot].RemoveCompatible(TempPlayerDict[Partner])
                            else:
                                logger.warning(f"Player {Partner} Not in Player list")
                    pass
            return TempPlayerDict
        except yaml.YAMLError as exc:
            logger.error(exc)
        return dict()

def getFileName() -> str:
    return str(time.strftime("%Y%m%d-%H%M%S")) + '.yaml'

def WriteYAMLOutFile(HamiltonTraveler:Graph, PlayerDict:dict[str,Player], outputdir='output'):
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)
    OutputYamlPath=os.path.join(outputdir,getFileName())
    with open(OutputYamlPath, "a") as stream:
        avgCompatibilityLenght=0
        dataDict=dict()
        for cur, nxt in zip (HamiltonTraveler.finishedPath, HamiltonTraveler.finishedPath [1:] + [ HamiltonTraveler.finishedPath[0]] ):
            ListOfCompatibility = PlayerDict[HamiltonTraveler.random_order_vertex_list[cur]].acceptable_worlds & PlayerDict[HamiltonTraveler.random_order_vertex_list[nxt]].acceptable_worlds
            dataDict[HamiltonTraveler.random_order_vertex_list[cur]] = dict()
            dataDict[HamiltonTraveler.random_order_vertex_list[cur]]['SendTo'] = HamiltonTraveler.random_order_vertex_list[nxt]
            dataDict[HamiltonTraveler.random_order_vertex_list[cur]]['Chooses'] = list(ListOfCompatibility)
            avgCompatibilityLenght+=len(ListOfCompatibility)
        avgCompatibilityLenght/=len(HamiltonTraveler.finishedPath)
        yaml.dump(dataDict,stream)
        logger.info(f"The Average Compatibility of This Generation is {avgCompatibilityLenght}")
        return OutputYamlPath

    

def WriteCSVFile(CycleYaml='output/output.yaml', CycleCSVPath='output/OutputCSV.dsv'):
    PlayerSlotsName = dict()
    with open(CycleYaml) as outputCycleStream:
        with open(CycleCSVPath, 'w') as CSVOutStream:
            try:
                yamlObject=yaml.safe_load(outputCycleStream)
                if isinstance(PlayerSlotsName ,list):
                    PlayerSlotsName.sort()
                for id, Slot in sorted(enumerate(yamlObject),  key=lambda x: x[1].lower()):
                    CSVOutStream.write(f"{Slot}..{yamlObject[Slot]['SendTo']}...{yamlObject[Slot]['Chooses']}\n")
            except yaml.YAMLError as exc:
                print(exc)
    

if __name__ == "__main__":
    logging.basicConfig(filename='logs/YamlParsing.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] %(levelname)s %(message)s',  datefmt='%I:%M:%S')
    for PlayerName,PlayerObj in ParseDSGYaml(True).items():
                if isinstance(PlayerObj, Player):
                    print(PlayerName,":",len(PlayerObj.CompatiblePlayers))
    