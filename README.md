# What's this?

This is a utility for planning a "Double Slot Goodness" exchange in an [Archipelago Multiworld Randomizer](archipelago.gg)

# How do you use this?

It currently has no commandline options, so you only ned to call the main file and it will read the `DSG-data.yaml` file, whereupon it will spit out either a 'no' or a 'yes' to let you know if it found a valid cycle

If it found a valid cycle, it will give you the name of the slots in order, such that the first one on the list will give a slot to the second, the second to the third and so on. The last slot name on the cycle will then give a slot to the first one in the cycle

For more information and Common Question You might have consider Reading the [FAQ](FAQ.md)

## YAML options

The basic structure of the YAML file needed is as follows
```yaml
SlotName: ["FirstPlayer", "SecondPlayer", "ThirdPlayer", "FourthPlayer"]
ExclusionList:
  ArbitraryListName: ["FirstPlayer", "FourthPlayer"]
Worlds:
  FirstWorld: ["FirstPlayer", "SecondPlayer", "ThirdPlayer", "FourthPlayer"]
  SecondWorld: ["FirstPlayer", "SecondPlayer", "ThirdPlayer", "FourthPlayer"]
  ThirdWorld: ["FirstPlayer", "SecondPlayer", "ThirdPlayer", "FourthPlayer"]
  FourthWorld: ["FirstPlayer", "SecondPlayer", "ThirdPlayer", "FourthPlayer"]
```
Alternatively instead of using flow collections you could write it out as

```yaml
SlotName: 
    - 'FirstPlayer'
    - 'SecondPlayer'
    - 'ThirdPlayer'
ExclusionList:
  ArbitraryListName: 
    - 'FirstPlayer'
    - 'FourthPlayer'
Worlds:
  FirstWorld: 
    - 'FirstPlayer'
    - 'SecondPlayer'
    - 'ThirdPlayer'
    - 'FourthPlayer'
  SecondWorld: 
    - 'FirstPlayer'
    - 'SecondPlayer'
    - 'ThirdPlayer'
    - 'FourthPlayer'
  ThirdWorld: 
    - 'FirstPlayer'
    - 'SecondPlayer'
    - 'ThirdPlayer'
    - 'FourthPlayer'
  FourthWorld:
    - 'FirstPlayer'
    - 'SecondPlayer'
    - 'ThirdPlayer'
    - 'FourthPlayer'
```

Any name not listed in `SlotName` shall be ignored. 

Any collection in `ExclusionList` will make any `SlotName` be unable to receive and give slots to any other slot in the same list. Useful if you have Player(s) that want to have more than 2 games at a time, but don't want to receive Slots from themselves.

You may add any arbitrary number of `SlotName` and `Worlds` entries, but keep in mind large numbers might take a while, specially since this is implemented on python

# Requirements

- pyyaml, If you have the [Archipelago launcher](https://github.com/ArchipelagoMW/Archipelago/) you may already have this installed