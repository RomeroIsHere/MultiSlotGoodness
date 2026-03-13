import yaml
from Players import Player

def ParseYaml() -> dict[str,Player]:
    with open("DSG-data.yaml") as stream:
        try:
            yamlObject=yaml.safe_load(stream)
            TempPlayerDict=dict()
            PlayerSlotsName =yamlObject.get('SlotName')
            # Add a Player with an ID to use as an index
            for id, Slot in enumerate(PlayerSlotsName):
                TempPlayerDict[Slot]=(Player(Slot, id))
            
            WorldList=yamlObject.get('Worlds')
            for WorldName in WorldList.keys():
                for Slot in WorldList[WorldName]:
                    TempPlayerDict[Slot].acceptable_worlds.add(WorldName)
                    for Partner in WorldList[WorldName]:
                        TempPlayerDict[Slot].AddToCompatible(TempPlayerDict[Partner])
            return TempPlayerDict
        except yaml.YAMLError as exc:
            print(exc)
        return dict()
if __name__ == "__main__":
    DictOfPlayers=dict()
    print(ParseYaml())
    
    