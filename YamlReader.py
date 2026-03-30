import yaml
from Players import Player

def ParseDSGYaml(shouldPrint=False) -> dict[str,Player]:
    print("Parsing YAML")
    with open("DSG-data.yaml") as stream:
        try:
            yamlObject=yaml.safe_load(stream)
            TempPlayerDict=dict() # [str,Player]
            PlayerSlotsName =yamlObject.get('SlotName')
            if shouldPrint:
                print("Number Of Players:",len(PlayerSlotsName))
            # Add a Player with an ID to use as an index
            for id, Slot in enumerate(PlayerSlotsName):
                TempPlayerDict[Slot]=(Player(Slot, id))
            
            WorldList=yamlObject.get('Worlds')
            if not (WorldList):
                print("No Worlds?")
            else:
                print("Has Worlds")
                for WorldName in WorldList.keys():
                    if shouldPrint:
                        print("World:",WorldName)
                    for Slot in WorldList[WorldName]:
                        # Check if Slot is One of the Players
                        if not (Slot in PlayerSlotsName):
                            if shouldPrint:
                                print("Player not in List:",Slot)
                        else:
                            #Since it is
                            if shouldPrint:
                                print("    Player:",Slot)
                            # Add it the World to the Player
                            TempPlayerDict[Slot].acceptable_worlds.add(WorldName)
                            
                            for Partner in WorldList[WorldName]:
                                # then add Every Compatible Player in List if their a Valid player
                                if (Partner in PlayerSlotsName):
                                    TempPlayerDict[Slot].AddToCompatible(TempPlayerDict[Partner])
                                else:
                                    if shouldPrint:
                                        print("Player not in List:",Partner)
            # Now Get the List of Exclusions
            ExcludeList=yamlObject.get('ExclusionList')
            if not ExcludeList:
                print("No exclusions to take care of")
            else:
                print("Handling Exclusions")
                for list in ExcludeList.keys():
                    if shouldPrint:
                        print("Excluding List:",list)
                    for Slot in ExcludeList[list]:
                        if shouldPrint:
                            print("Handling:",Slot)
                        for Partner in ExcludeList[list]:
                            if shouldPrint:
                                print("Excluding Partner:",Partner)
                            if (Partner in PlayerSlotsName):
                                TempPlayerDict[Slot].RemoveCompatible(TempPlayerDict[Partner])
                            else:
                                if shouldPrint:
                                    print(Partner, "Not in PlayerList")
                    pass
            return TempPlayerDict
        except yaml.YAMLError as exc:
            print(exc)
        return dict()
if __name__ == "__main__":
    DictOfPlayers=dict()
    for PlayerName,PlayerObj in ParseDSGYaml(True).items():
                if isinstance(PlayerObj, Player):
                    print(PlayerName,":",len(PlayerObj.CompatiblePlayers))
    