import yaml
from Players import Player
from Worlds import World

with open("DSG-data.yaml") as stream:
    try:
        yamlObject=yaml.safe_load(stream)
        PlayerList=dict()
        PlayerSlotsName =yamlObject.get('SlotName')
        for id, Slot in enumerate(PlayerSlotsName):
            PlayerList[Slot]=(Player(Slot, id))
        WorldList=dict()
        for AvaibleWorlds in yamlObject.get('Worlds'):
            WorldList[AvaibleWorlds]=(yamlObject.get(AvaibleWorlds))
            for Slot in WorldList[AvaibleWorlds]:
                PlayerList[Slot].acceptable_worlds.add(AvaibleWorlds)
        print(PlayerList)
        print(WorldList)
    except yaml.YAMLError as exc:
        print(exc)