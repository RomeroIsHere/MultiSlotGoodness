import yaml
from Players import Player

def ParseDSGYaml() -> dict[str,Player]:
    print("Parsing YAML")
    with open("DSG-data.yaml") as stream:
        try:
            yamlObject=yaml.safe_load(stream)
            TempPlayerDict=dict() # [str,Player]
            PlayerSlotsName =yamlObject.get('SlotName')
            # Add a Player with an ID to use as an index
            for id, Slot in enumerate(PlayerSlotsName):
                TempPlayerDict[Slot]=(Player(Slot, id))
            
            WorldList=yamlObject.get('Worlds')
            for WorldName in WorldList.keys():
                print("World:",WorldName)
                for Slot in WorldList[WorldName]:
                    if not (Slot in PlayerSlotsName):
                         print("Player not in List:",Slot)
                    else:
                        print("    Player:",Slot)
                        TempPlayerDict[Slot].acceptable_worlds.add(WorldName)
                        for Partner in WorldList[WorldName]:
                            if (Partner in PlayerSlotsName):
                                TempPlayerDict[Slot].AddToCompatible(TempPlayerDict[Partner])
                            else:
                                print("Player not in List:",Partner)
            
            return TempPlayerDict
        except yaml.YAMLError as exc:
            print(exc)
        return dict()
if __name__ == "__main__":
    DictOfPlayers=dict()
    for PlayerName,PlayerObj in ParseDSGYaml().items():
                if isinstance(PlayerObj, Player):
                    print(PlayerName,":",len(PlayerObj.CompatiblePlayers))
    