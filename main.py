import logging
import DSGManualGameCompatibility
from Menu import Menu
from Models import Player
from DSGFileHandler import OutputHandler, InputHandler, Utility
import DSGTestAverageCompatibility, DSGGenerateCycle, DSGRenamePlayerFiles

def RenameYamls():
    renamedict=InputHandler.ParseRenameYaml()
    OutputHandler.RenameAndCopyYAML(renamedict)

if __name__ == "__main__":
    Utility.MakeDir("logs")
    logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    listOfActions=[
        ('Check Number of Compatible Partner', InputHandler.CompatiblePlayers),
        ('Generate Cycle', DSGGenerateCycle.GenerateCycle),
        ('Rename Collected Yamls', DSGRenamePlayerFiles.RenameYamls),
        ('Manually Check Players', DSGManualGameCompatibility.Main),
        ('Test Average Game Compatibility of Cycles', DSGTestAverageCompatibility.mainTest)

    ]
    Menu.menu("Double Slot Goodness Tool",listOfActions)