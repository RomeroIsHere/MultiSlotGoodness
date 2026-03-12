import yaml
from Players import Player

def ParseYaml(PlayerList:dict[str,Player]):
    with open("DSG-data.yaml") as stream:
        try:
            yamlObject=yaml.safe_load(stream)
            PlayerList=dict()
            PlayerSlotsName =yamlObject.get('SlotName')
            # Add a Player with an ID to use as an index
            for id, Slot in enumerate(PlayerSlotsName):
                PlayerList[Slot]=(Player(Slot, id))
            
            WorldList=dict()
            # For every Candidate world
            for AvaibleWorlds in yamlObject.get('Worlds'):
                # Create a New World Entry, with the List of Players in the Dict
                WorldList[AvaibleWorlds]=(yamlObject.get(AvaibleWorlds))
                # Now Add the World Name to Every Player that can play it
                for Slot in WorldList[AvaibleWorlds]:
                    # could be ignored if no logkeeping or Change in behaviour i guess
                    PlayerList[Slot].acceptable_worlds.add(AvaibleWorlds)
                    for Partner in WorldList[AvaibleWorlds]:
                        PlayerList[Slot].AddToCompatible(PlayerList[Partner])
            print(PlayerList)
            for slots in PlayerSlotsName:
                print("Current Slot:" + slots)
                PlayerList[slots].printCompatible()
            print(WorldList)

        except yaml.YAMLError as exc:
            print(exc)