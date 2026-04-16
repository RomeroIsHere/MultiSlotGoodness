import logging
import shutil
from sympy import false
import yaml
import os
from DSGFileHandler import InputHandler
from Models import Graph
from Models import Player
from . import Utility
logger = logging.getLogger(__name__)

def WriteYAMLOutFile(HamiltonTraveler:Graph, PlayerDict:dict[str,Player], outputdir='output'):
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)
    OutputYamlPath=os.path.join(outputdir, Utility.getFileName())
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
        print(f"Wrote File to {OutputYamlPath}")
        return OutputYamlPath

    

def WriteCSVFile(CycleYaml='output/output.yaml', CycleCSVPath='output/OutputCSV.dsv'):
    PlayerSlotsName = dict()
    yamlObject=InputHandler.ParseCycleYamls(CycleYaml)
    with open(CycleCSVPath, 'w') as CSVOutStream:
        try:
            if isinstance(PlayerSlotsName ,list):
                PlayerSlotsName.sort()
            for id, Slot in sorted(enumerate(yamlObject),  key=lambda x: x[1].lower()):
                CSVOutStream.write(f"{Slot}..{yamlObject[Slot]['SendTo']}...{yamlObject[Slot]['Chooses']}\n")
        except yaml.YAMLError as exc:
            print(exc)

def CopyDirTree(PlayerYamlsDir="YAML/Originals", RenamedYamlsDir="YAML/Copy"):
    Utility.MakeDir(PlayerYamlsDir)
    Utility.MakeDir(RenamedYamlsDir)
    shutil.copytree(PlayerYamlsDir,RenamedYamlsDir, dirs_exist_ok=True)


def RenameAndCopyYAML(RenamerDict:dict,PlayerYamlsDir="YAML/Originals", RenamedYamlsDir="YAML/Copy"):
    CopyDirTree(PlayerYamlsDir, RenamedYamlsDir)
    for _, _, files in os.walk(RenamedYamlsDir):
        for file in files:
            fileWithPath=os.path.join(RenamedYamlsDir, file)
            YamlObject=None
            with open(fileWithPath) as APYAMLStream:
                try:
                    YamlObject=yaml.safe_load(APYAMLStream)
                    SlotName=YamlObject.get("name")
                    if SlotName in RenamerDict:
                        YamlObject["name"]=RenamerDict[SlotName]
                except:
                    pass
            with open(fileWithPath, "w") as APYAMLStrem:
                try:
                    yaml.dump(YamlObject, APYAMLStrem, sort_keys=false)
                except:
                    pass