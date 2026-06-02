import logging
import shutil
from typing import Iterator
from sympy import false
import yaml
import os
from DSGFileHandler import InputHandler
from Models import Graph
from Models import Player
from . import Utility
logger = logging.getLogger(__name__)

def WriteYAMLOutFile(HamiltonTraveler:Graph, PlayerDict:dict[str,Player], OutputFilename:str="",outputdir='output'):
    if not os.path.isdir(outputdir):
        os.makedirs(outputdir)
    if not OutputFilename:
        OutputYamlPath=os.path.join(outputdir, Utility.getFileName())
    else:
        OutputYamlPath=os.path.join(outputdir, OutputFilename)
    with open(OutputYamlPath, "w") as stream:
        avgCompatibilityLenght=0
        dataDict=dict()
        for cur, nxt in zip (HamiltonTraveler.finishedPath, HamiltonTraveler.finishedPath [1:] + [ HamiltonTraveler.finishedPath[0]] ):
            ListOfCompatibility = PlayerDict[str(cur)].acceptable_worlds & PlayerDict[str(nxt)].acceptable_worlds
            dataDict[cur] = dict()
            dataDict[cur]['SendTo'] = nxt
            dataDict[cur]['Chooses'] = list(ListOfCompatibility)
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
def RenameAndStripYAML(PlayerYamlsDir="YAML/Originals", RenamedYamlsDir="YAML/Copy"):
    CopyDirTree(PlayerYamlsDir, RenamedYamlsDir)
    for _, _, files in os.walk(RenamedYamlsDir):
        for file in files:
            fileWithPath=os.path.join(RenamedYamlsDir, file)
            YamlObjectGenerator:Iterator|None=None
            SpecificYamlObjectsList:list=list()
            with open(fileWithPath) as APYAMLStream:
                try:
                    YamlObjectGenerator=yaml.safe_load_all(APYAMLStream)
                    for mini in YamlObjectGenerator:
                        gameName=mini.get("game")
                        FullOptionSet=mini.get(gameName)
                        FullOptionSet.pop("plando_items",None)
                        mini[gameName]=FullOptionSet
                        SpecificYamlObjectsList.append(mini)
                except Exception as e:
                    print(f"Error at {fileWithPath}")
                    print(f"Error is {e}")
                    logger.error(f"Error at {fileWithPath}")
                    logger.error(f"Error is {e}")
                    pass
            with open(fileWithPath, "w") as APYAMLStrem:
                try:
                    yaml.dump_all(SpecificYamlObjectsList, APYAMLStrem, sort_keys=false)
                except:
                    pass