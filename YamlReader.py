import yaml
from Players import Player
from Worlds import World

with open("DSG-data.yaml") as stream:
    try:
        yamlObject=yaml.safe_load(stream)
        print(yamlObject)
        PlayerList=set()
        for Slot in yamlObject.get('SlotName'):
            PlayerList.add(Player(Slot))
        WorldList=set()
        for AvaibleWorlds in yamlObject.get('Worlds'):
            WorldList.add(World(AvaibleWorlds))

        print(PlayerList)
        print(WorldList)
    except yaml.YAMLError as exc:
        print(exc)