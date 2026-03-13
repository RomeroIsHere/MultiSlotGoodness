import yaml
from Players import Player

def ParseYaml(PlayerAdjacencyDict:dict[str,list[str]]):
    with open("DSG-data.yaml") as stream:
        try:
            yamlObject=yaml.safe_load(stream)
            TempPlayerList=dict()
            PlayerSlotsName =yamlObject.get('SlotName')
            # Add a Player with an ID to use as an index
            for id, Slot in enumerate(PlayerSlotsName):
                TempPlayerList[Slot]=(Player(Slot, id))
            
            WorldList=yamlObject.get('Worlds')
            for WorldName in WorldList.keys():
                for Slot in WorldList[WorldName]:
                    TempPlayerList[Slot].acceptable_worlds.add(WorldName)
                    for Partner in WorldList[WorldName]:
                        TempPlayerList[Slot].AddToCompatible(TempPlayerList[Partner])
            for Slot in PlayerSlotsName:
                PlayerAdjacencyDict[Slot]=TempPlayerList[Slot].CompatiblePlayers
            return TempPlayerList
        except yaml.YAMLError as exc:
            print(exc)
if __name__ == "__main__":
    DictOfPlayers=dict()
    ParseYaml(DictOfPlayers)
    print(DictOfPlayers)
    