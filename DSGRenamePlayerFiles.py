import logging
from DSGFileHandler import InputHandler, OutputHandler, Utility
logger=logging.getLogger(__name__)

def RenameYamls():
    renamedict=InputHandler.ParseRenameYaml()
    OutputHandler.RenameAndCopyYAML(renamedict)
if __name__ == "__main__":
    Utility.MakeDir("logs")
    logging.basicConfig(filename='logs/renaming.log', encoding='utf-8', level=logging.INFO, format='[%(asctime)s]%(name)s:%(levelname)s %(message)s',  datefmt='%I:%M:%S')
    RenameYamls()