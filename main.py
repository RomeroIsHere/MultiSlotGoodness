import logging
import DSGManualGameCompatibility
from Menu import Menu
from DSGFileHandler import OutputHandler, InputHandler, Utility
import DSGTestAverageCompatibility, DSGGenerateCycle, DSGRenamePlayerFiles, SYEREmovePlando

def RenameYamls():
    renamedict=InputHandler.ParseRenameYaml()
    OutputHandler.RenameAndCopyYAML(renamedict)

if __name__ == "__main__":
    Utility.MakeDir("logs")
    logging.basicConfig(filename='logs/main.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    listOfActions=[
        ('Check Number of Compatible Partner', InputHandler.CompatiblePlayers),
        ('Generate Cycle', DSGGenerateCycle.GenerationMenu),
        ('Rename Collected Yamls', DSGRenamePlayerFiles.RenameYamls),
        ('Strip Plando Blocks from Collected Yamls', SYEREmovePlando.StripPlando),
        ('Manually Check Players', DSGManualGameCompatibility.Main),
        ('Test Average Game Compatibility of Cycles', DSGTestAverageCompatibility.mainTest)

    ]
    Menu.menu("Double Slot Goodness Tool",listOfActions)