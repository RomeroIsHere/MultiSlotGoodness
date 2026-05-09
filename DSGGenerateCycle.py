import logging
from os import close
from DSGFileHandler import InputHandler, OutputHandler, Utility
from Models import Graph, Player
from Menu import Menu
from typing import Any, Callable

logger=logging.getLogger(__name__)

def GenerationMenu():
    print(f"Functionality Not Integrated Yet")
    logger.error(f"Functionality Not Integrated Yet")
    listOfActions=[
        ('Generate Random Compatible Cycle', GenerateCycle),
        ("Generate Alphabetized Bias Cycle", GenerateAlphabetizedCycle),
        ("Generate # Game Count Bias Cycle", GenerateGameCount),
        ("Generate Compatibility Bias Cycle", GenerateGameCompatibility),
    ]
    Menu.menu('\nHamiltonian Path Generation',listOfActions)

    pass

def GenerateAlphabetizedCycle():
    GenerateCycle(lambda x:x)


def GenerateGameCount():
    PlayerDict=InputHandler.ParseDSGYaml()
    def Closure(x:str):
        return len(PlayerDict.get(x,Player("Unknown",-1)).acceptable_worlds)
    GenerateCycle(Closure)

def GenerateGameCompatibility():
    PlayerDict=InputHandler.ParseDSGYaml()
    def Closure(x:str):
        key=0
        for playerob in PlayerDict.values():
            key+=len(playerob.acceptable_worlds.intersection(PlayerDict.get(x,Player("Unknown",-1)).acceptable_worlds))
        print(key)
        return key
    GenerateCycle(Closure)

def GenerateCycle(key:Callable[[str], Any]|None=None):
    logger.info("Starting Generation")
    print("Starting Generation")
    SlotNamesAdjacencyDict=dict()
    PlayerDict=InputHandler.ParseDSGYaml()
    logger.info("Succesfully got PlayerDict")
    logger.debug("Turning PlayerDict into and Adjacency Dict")

    for Slot in PlayerDict.keys():
        SlotNamesAdjacencyDict[Slot]=PlayerDict[Slot].CompatiblePlayers
    HamiltonTraveler=Graph(SlotNamesAdjacencyDict, key=key)
    logger.info("Finding Cycle")
    print("Finding Cycle")
    if HamiltonTraveler.find_hamiltonian_cycle():
        logger.info("Found Hamiltonian Cycle")
        logger.info("Writing to file")
        print("Found Cycle")
        OutputFile = OutputHandler.WriteYAMLOutFile(HamiltonTraveler, PlayerDict)
        OutputHandler.WriteYAMLOutFile(HamiltonTraveler, PlayerDict, OutputFilename="DSG-cycle.yaml", outputdir="YAML")
        logger.info(f"Wrote Cycle as YAML to {OutputFile}")
        OutputHandler.WriteCSVFile(OutputFile, OutputFile + '.dsv')
    else:
        print("\n\n**NO CYCLE FOUND**\n\n")

if __name__ == "__main__":
    Utility.MakeDir("logs")
    logging.basicConfig(filename='logs/generate.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    GenerateCycle()
    