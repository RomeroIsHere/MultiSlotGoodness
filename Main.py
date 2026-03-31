import logging
import YamlFilesHandling
from Players import Player
from Graph import Graph

logger=logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    logger.info("Starting Application")
    SlotNamesAdjacencyDict=dict()
    PlayerDict=YamlFilesHandling.ParseDSGYaml()
    logger.info("Succesfully got PlayerDict")
    logger.debug("Turning PlayerDict into and Adjacency Dict")

    for Slot in PlayerDict.keys():
        SlotNamesAdjacencyDict[Slot]=PlayerDict[Slot].CompatiblePlayers
    HamiltonTraveler=Graph(SlotNamesAdjacencyDict)
    logger.info("Finding Cycle")
    if HamiltonTraveler.find_hamiltonian_cycle():
        logger.info("Found Hamiltonian Cycle")
        logger.info("Writing to file")
        OutputFile = YamlFilesHandling.WriteYAMLOutFile(HamiltonTraveler, PlayerDict)
        logger.info(f"Wrote Cycle as YAML to {OutputFile}")
        YamlFilesHandling.WriteCSVFile(OutputFile)
