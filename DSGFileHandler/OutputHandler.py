import logging
import yaml
import os
from datetime import datetime
from Models import Graph
from Models import Player
logger = logging.getLogger(__name__)


def getFileName() -> str:
    return str(datetime.now().strftime('%Y-%m-%d-%H%M%S%f')[:-3]) + '.yaml'

def MakeLogDir(outputdir='logs'):
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)

def WriteYAMLOutFile(HamiltonTraveler:Graph, PlayerDict:dict[str,Player], outputdir='output'):
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)
    OutputYamlPath=os.path.join(outputdir,getFileName())
    with open(OutputYamlPath, "w") as stream:
        avgCompatibilityLenght=0
        dataDict=dict()
        for cur, nxt in zip (HamiltonTraveler.finishedPath, HamiltonTraveler.finishedPath [1:] + [ HamiltonTraveler.finishedPath[0]] ):
            ListOfCompatibility = PlayerDict[HamiltonTraveler.random_order_vertex_list[cur]].acceptable_worlds & PlayerDict[HamiltonTraveler.random_order_vertex_list[nxt]].acceptable_worlds
            dataDict[HamiltonTraveler.random_order_vertex_list[cur]] = dict()
            dataDict[HamiltonTraveler.random_order_vertex_list[cur]]['SendTo'] = HamiltonTraveler.random_order_vertex_list[nxt]
            dataDict[HamiltonTraveler.random_order_vertex_list[cur]]['Chooses'] = list(ListOfCompatibility)
            avgCompatibilityLenght+=len(ListOfCompatibility)
        avgCompatibilityLenght/=len(HamiltonTraveler.finishedPath)
        yaml.dump(dataDict,stream)
        logger.info(f"The Average Compatibility of This Generation is {avgCompatibilityLenght}")
        return OutputYamlPath

    

def WriteCSVFile(CycleYaml='output/output.yaml', CycleCSVPath='output/OutputCSV.dsv'):
    PlayerSlotsName = dict()
    with open(CycleYaml) as outputCycleStream:
        with open(CycleCSVPath, 'w') as CSVOutStream:
            try:
                yamlObject=yaml.safe_load(outputCycleStream)
                if isinstance(PlayerSlotsName ,list):
                    PlayerSlotsName.sort()
                for id, Slot in sorted(enumerate(yamlObject),  key=lambda x: x[1].lower()):
                    CSVOutStream.write(f"{Slot}..{yamlObject[Slot]['SendTo']}...{yamlObject[Slot]['Chooses']}\n")
            except yaml.YAMLError as exc:
                print(exc)