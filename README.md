# What's this?

This is a utility for planning a "Double Slot Goodness" exchange in an [Archipelago Multiworld Randomizer](archipelago.gg)

# Installation

You currently need to run this Tool from Source 
```sh
git clone https://github.com/RomeroIsHere/MultiSlotGoodness.git
pip install pyyaml
cd MultiSlotgoodness
```
then run via
```sh
py main.py
```

# How do you use this?

It currently has no commandline options, so you only ned to call the main file and select 'Generate Cycle', which will read the `DSG-data.yaml` file inside the `YAML` Folder, whereupon it will spit out a file in the `output` folder, to let you know if it found a valid cycle. Using This will let you know who will give a YAML to whom

If it found a valid cycle, it will give you the name of the slots in order, such that the first one on the list will give a slot to the second, the second to the third and so on. The last slot name on the cycle will then give a slot to the first one in the cycle

If you want to Rename Collected YAMLs. you will need to fill `DSG-rename.yaml` with the renaming Rules suchs as
```yaml
OriginalName: Renamed
AnotherOriginalName: Renamed
```

For more information and Common Question You might have consider Reading the [FAQ](FAQ.md)

## YAML options

The basic structure of the YAML file needed is as follows
```yaml
SlotName: ["FirstPlayer", "SecondPlayer", "ThirdPlayer", "FourthPlayer"]
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
Worlds:
  FirstWorld: 
    - 'FirstPlayer'
    - 'SecondPlayer'
    - 'FourthPlayer'
  SecondWorld: 
    - 'FirstPlayer'
    - 'ThirdPlayer'
    - 'FourthPlayer'
  ThirdWorld: 
    - 'FirstPlayer'
    - 'SecondPlayer'
    - 'ThirdPlayer'
  FourthWorld:
    - 'FirstPlayer'
    - 'SecondPlayer'
    - 'ThirdPlayer'
    - 'FourthPlayer'
```

Any name not listed in `SlotName` shall be ignored. 

You may add any arbitrary number of `SlotName` and `Worlds` entries, but keep in mind large numbers might take a while, specially since this is implemented on python

## Additional Option

These are options that Will be Ignored if Not Included in your `DSG-data.yaml`. They extend the basic Functionality for actual Use Cases

### Exclusion Lists

```yaml
ExclusionList:
  ArbitraryListName: 
    - 'FirstPlayer'
    - 'FourthPlayer'
```
Any collection in `ExclusionList` will make any `SlotName` be unable to receive and give slots to any other slot in the same list. Useful if you have Player(s) that want to have more than 2 games at a time, but don't want to receive Slots from themselves.

In this Example `FirstPlayer` and `FourthPlayer` will be unable to give eachother any Slots, from any game, even if they're Both included in a World inside `Worlds`. This does not Stop them from giving Anyone else any slot in those Games.

### Game Variety Enforcer

```yaml
MinimumGameVarietyScore: 0
```
> [!NOTE]
> The Default for this is 0. It will Let Compatibility Calculation Run through Normally.
> Pulling this to 1 will make it behave identically but Start taking into account the number of Compatible Games
> With values 2 and above it will start culling player compatibility lower than the value set.

This will make it So that For 2 People to be able to Give eachother a Slot they MUST have at least `MinimumGameVarietyScore` Number of Games in Common.

If you have a highly connected group This Option Can give you a Slot with a Higher Average Compatibility between players.

In a More Sparsely Connected Group it might not be Worth it to Pull this Higher.


> [!CAUTION]
> This option might make it Fully impossible for you to Generate a Cycle if you set it high Enough, If your Generation is Taking too long or It fails, Consider Lowering this or Leaving it In default


# Requirements

- pyyaml, If you have the [Archipelago launcher](https://github.com/ArchipelagoMW/Archipelago/) you may already have this installed
