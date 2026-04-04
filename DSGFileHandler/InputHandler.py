import logging
import yaml
import Models.Players as Players
from Models import Player
from . import OutputHandler

logger=logging.getLogger(__name__)

def ParseDSGYaml(DSGDataPath="Players/DSG-data.yaml") -> dict[str,Player]:
    
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
            Players.UpdateGlobalVarietyCount(yamlObject.get('MinimumGameVarietyScore', -1))
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


def ParseRenameYaml():
    pass

if __name__ == "__main__":
    OutputHandler.MakeLogDir()
    logging.basicConfig(filename='logs/YamlParsing.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s] %(levelname)s %(message)s',  datefmt='%I:%M:%S')
    for PlayerName,PlayerObj in ParseDSGYaml().items():
                if isinstance(PlayerObj, Player):
                    print(f"{PlayerName}: {len(PlayerObj.CompatiblePlayers)}")
    