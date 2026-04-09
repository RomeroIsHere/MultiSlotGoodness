import logging
from DSGFileHandler import InputHandler, OutputHandler, Utility
from Models import Graph

logger=logging.getLogger(__name__)

def GenerateCycle():
    logger.info("Starting Generation")
    SlotNamesAdjacencyDict=dict()
    PlayerDict=InputHandler.ParseDSGYaml()
    logger.info("Succesfully got PlayerDict")
    logger.debug("Turning PlayerDict into and Adjacency Dict")

    for Slot in PlayerDict.keys():
        SlotNamesAdjacencyDict[Slot]=PlayerDict[Slot].CompatiblePlayers
    HamiltonTraveler=Graph(SlotNamesAdjacencyDict)
    logger.info("Finding Cycle")
    if HamiltonTraveler.find_hamiltonian_cycle():
        logger.info("Found Hamiltonian Cycle")
        logger.info("Writing to file")
        OutputFile = OutputHandler.WriteYAMLOutFile(HamiltonTraveler, PlayerDict)
        logger.info(f"Wrote Cycle as YAML to {OutputFile}")
        OutputHandler.WriteCSVFile(OutputFile, OutputFile + '.dsv')

if __name__ == "__main__":
    Utility.MakeDir("logs")
    logging.basicConfig(filename='logs/generate.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    GenerateCycle()
    